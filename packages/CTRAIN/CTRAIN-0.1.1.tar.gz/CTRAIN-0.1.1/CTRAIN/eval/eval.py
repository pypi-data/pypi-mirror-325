import json
import os
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import numpy as np

import shutil

from auto_LiRPA import PerturbationLpNorm
from sklearn.metrics import accuracy_score
from tqdm import tqdm

from CTRAIN.bound import bound_ibp, bound_crown, bound_crown_ibp
from CTRAIN.attacks import pgd_attack
from CTRAIN.complete_verification.abCROWN.util import instances_to_vnnlib, get_abcrown_standard_conf
from CTRAIN.complete_verification.abCROWN.verify import limited_abcrown_eval, abcrown_eval
from CTRAIN.util import export_onnx

def eval_acc(model, test_loader, test_samples=np.inf):
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            if total >= test_samples:
                break
            batch_indices = min(len(target), test_samples - total)
            data = data[:batch_indices]
            target = target[:batch_indices]
            
            data, target = data.to(device), target.to(device)
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)

            correct += (predicted == target).sum().item()

    test_samples = min(test_samples, total)
    # print(f'Accuracy of the standard model on the first {test_samples} test images: {correct / test_samples:.4f}')
    return correct / test_samples

def eval_ibp(model, eps, data_loader, n_classes=10, test_samples=np.inf, device='cuda'):
    certified = 0
    total_images = 0
    for batch_idx, (data, targets) in tqdm(enumerate(data_loader)):
        if total_images >= test_samples:
            continue
        
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data + eps, data_loader.min, data_loader.max).to(device))
        data, targets = data.to(device), targets.to(device)

        lb, ub = bound_ibp(
            model=model,
            ptb=ptb,
            data=data,
            target=targets,
            n_classes=n_classes,
            reuse_input=False
        )
        no_certified = torch.sum((lb > 0).all(dim=1)).item()
        # no_falsified = torch.sum((ub < 0).any(dim=1)).item()
        certified += no_certified
        
        total_images += len(targets)
    
    return certified, total_images

def eval_crown_ibp(model, eps, data_loader, n_classes=10, test_samples=np.inf, device='cuda'):
    certified = 0
    total_images = 0
    for batch_idx, (data, targets) in tqdm(enumerate(data_loader)):
        if total_images >= test_samples:
            continue
        
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data + eps, data_loader.min, data_loader.max).to(device))
        data, targets = data.to(device), targets.to(device)
        
        lb, ub = bound_crown_ibp(
            model=model,
            ptb=ptb,
            data=data,
            target=targets,
            n_classes=n_classes,
            reuse_input=False
        )
        no_certified = torch.sum((lb > 0).all(dim=1)).item()
        # no_falsified = torch.sum((ub < 0).any(dim=1)).item()
        certified += no_certified
        
        total_images += len(targets)
    
    return certified, total_images


def eval_crown(model, eps, data_loader, n_classes=10, test_samples=np.inf, device='cuda'):
    # IMPORTANT: Data Loader Batch Size must match Bounding Batch Size when using CROWN for evaluation (not important for IBP)
    crown_data_loader = DataLoader(data_loader.dataset, batch_size=1, shuffle=False)
    crown_data_loader.max, crown_data_loader.min, crown_data_loader.std = data_loader.max, data_loader.min, data_loader.std
    certified = 0
    total_images = 0
    for batch_idx, (data, targets) in tqdm(enumerate(crown_data_loader)):
        if total_images >= test_samples:
            continue
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data + eps, data_loader.min, data_loader.max).to(device))
        data, targets = data.to(device), targets.to(device)
        lb, ub = bound_crown(
            model=model,
            ptb=ptb,
            data=data,
            target=targets,
            n_classes=n_classes,
            reuse_input=False
        )
        no_certified = torch.sum((lb > 0).all(dim=1)).item()
        # no_falsified = torch.sum((ub < 0).any(dim=1)).item()
        certified += no_certified
        
        total_images += len(targets)
    
    return certified, total_images

def eval_complete_abcrown(model, eps_std, data_loader, n_classes=10, input_shape=[1, 28, 28], test_samples=np.inf, timeout=1000, no_cores=28, abcrown_batch_size=512, separate_abcrown_process=False, device='cuda'):
    
    no_certified, total_images, certified = eval_adaptive(model=model, eps=eps_std, data_loader=data_loader, n_classes=n_classes, test_samples=test_samples, device=device)
    adv_acc, adv_sample_found = eval_adversarial(model=model, data_loader=data_loader, eps=eps_std, n_classes=n_classes, device=device, test_samples=test_samples, return_adv_indices=True)
    adv_sample_found = torch.tensor(adv_sample_found)
    total_images = 0
        
    batch_size = data_loader.batch_size
    
    std_config = get_abcrown_standard_conf(timeout=timeout, no_cores=no_cores)
    std_config['solver']['batch_size'] = abcrown_batch_size
    
    os.makedirs('/tmp/abCROWN/', exist_ok=True)
    
    export_onnx(
        model=model,
        file_name='/tmp/abCROWN_model.onnx',
        batch_size=1, 
        input_shape=input_shape
    )
    
    for batch_idx, (data, targets) in tqdm(enumerate(data_loader)):
        if total_images >= test_samples:
            break
        
        batch_indices = min(len(targets), test_samples - total_images)
        data = data[:batch_indices]
        targets = targets[:batch_indices]
        total_images += len(targets)
        
        print(f"BATCH {batch_idx}")
        
        clean_pred = torch.argmax(model(data.to(device)), dim=1)
        clean_correct = clean_pred.cpu() == targets
        
        if certified[batch_idx * batch_size:(batch_idx + 1) * batch_size].all():
            continue
        
        os.makedirs(f'/tmp/vnnlib_{batch_idx}/', exist_ok=True)
        
        vnnlib_batch = instances_to_vnnlib(
            indices=[i for i in range(len(targets)) if not certified[batch_idx * batch_size + i] and not adv_sample_found[batch_idx * batch_size + i] and clean_correct[i]],
            data=[(img, target) for img, target in zip(data, targets)],
            vnnlib_path=f'/tmp/vnnlib_{batch_idx}/',
            experiment_name='Experiment',
            eps=eps_std * data_loader.std,
            eps_temp=eps_std,
            data_min=data_loader.min,
            data_max=data_loader.max,
            no_classes=n_classes
        )
        vnnlib_indices = [batch_idx * batch_size + i for i in range(len(targets)) if not certified[batch_idx * batch_size + i] and not adv_sample_found[batch_idx * batch_size + i] and clean_correct[i]]
        print(vnnlib_indices)
        for idx, vnn_instance in zip(vnnlib_indices, vnnlib_batch):
            if separate_abcrown_process:
                running_time, result = limited_abcrown_eval(
                    # work_dir='/tmp/abCROWN',
                    config=std_config,
                    seed=42,
                    instance=vnn_instance,
                    vnnlib_path=f'/tmp/vnnlib_{batch_idx}',
                    model_path=None,
                    model_name=None,
                    model_onnx_path='/tmp/abCROWN_model.onnx',
                    input_shape=[-1] + input_shape[1:4],
                    timeout=timeout,
                    no_cores=no_cores,
                    par_factor=1
                )
            else:
                running_time, result = abcrown_eval(
                    # work_dir='/tmp/abCROWN',
                    config=std_config,
                    seed=42,
                    instance=vnn_instance,
                    vnnlib_path=f'/tmp/vnnlib_{batch_idx}',
                    model_path=None,
                    model_name=None,
                    model_onnx_path='/tmp/abCROWN_model.onnx',
                    input_shape=[-1] + input_shape[1:4],
                    timeout=timeout,
                    no_cores=no_cores,
                    par_factor=1
                )
            print(running_time, result)
            if result == 'unsat':
                no_certified += 1
                certified[idx] = True
            if result == 'sat':
                adv_sample_found[idx] = True
        
        shutil.rmtree(f"/tmp/vnnlib_{batch_idx}/")
    
    if test_samples < np.inf:
        certified = certified[:test_samples]
    no_certified = torch.sum(certified)    
    no_counterexample = torch.sum(adv_sample_found)
            
    certified_acc = (no_certified / test_samples).cpu().item() if torch.is_tensor(certified) else certified / test_samples
    adv_acc = (test_samples  - no_counterexample) / test_samples
    if torch.is_tensor(adv_acc):
        adv_acc = adv_acc.item()
    
    return certified_acc, adv_acc

def eval_adaptive(model, eps, data_loader, n_classes=10, test_samples=np.inf, device='cuda', methods=["IBP", "CROWN_IBP", "CROWN"]):
    assert methods is not None and len(methods) > 1, "Please provide at least one bounding method!"

    certified = torch.tensor([], device=device)
    total_images = 0
    
    crown_data_loader = DataLoader(data_loader.dataset, batch_size=1, shuffle=False)
    crown_data_loader.max, crown_data_loader.min, crown_data_loader.std = data_loader.max, data_loader.min, data_loader.std
    
    for batch_idx, (data, targets) in tqdm(enumerate(data_loader)):
        certified_idx = torch.zeros(len(data), device=device, dtype=torch.bool)
        
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data + eps, data_loader.min, data_loader.max).to(device))
        data, targets = data.to(device), targets.to(device)
        if batch_idx * data_loader.batch_size >= test_samples:
            continue
        
        total_images += len(targets)
        
        if "IBP" in methods:
            lb, ub = bound_ibp(
                model=model,
                ptb=ptb,
                data=data,
                target=targets,
                n_classes=n_classes,
                reuse_input=False
            )
            certified_idx[(lb > 0).all(dim=1)] = True
        
        data = data.to('cpu')
        certified_idx = certified_idx.to("cpu")
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data[~certified_idx] - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data[~certified_idx] + eps, data_loader.min, data_loader.max).to(device))
        data = data.to(device)
        certified_idx = certified_idx.to(device)
        
        if len(certified_idx) < len(targets) and "CROWN-IBP" in methods:        
            lb, ub = bound_crown_ibp(
                model=model,
                ptb=ptb,
                data=data[~certified_idx],
                target=targets[~certified_idx],
                n_classes=n_classes,
                reuse_input=False
            )
            certified_idx[~certified_idx] = (lb > 0).all(dim=1)
            
        certified = torch.concatenate((certified, certified_idx))
    
    print(f"certified {torch.sum(certified).item()} / {len(certified)} using IBP", flush=True)
    
    for batch_idx, (data, targets) in tqdm(enumerate(crown_data_loader)):
        if batch_idx >= test_samples:
            continue
        if certified[batch_idx] or not ("CROWN" in methods):
            continue
        
        ptb = PerturbationLpNorm(eps=eps, norm=np.inf, x_L=torch.clamp(data - eps, data_loader.min, data_loader.max).to(device), x_U=torch.clamp(data + eps, data_loader.min, data_loader.max).to(device))
        data, targets = data.to(device), targets.to(device)
        
        lb, ub = bound_crown(
            model=model,
            ptb=ptb,
            data=data,
            target=targets,
            n_classes=n_classes,
            reuse_input=False
        )
        instance_certified = (lb > 0).all(dim=1).item()
        certified[batch_idx] = instance_certified
    
    if test_samples < np.inf:
        certified = certified[:test_samples]
    no_certified = torch.sum(certified)            
    total_images = len(certified)
    
    if 'CROWN' in methods:
        print(f"certified {torch.sum(certified).item()} / {len(certified)} after using CROWN", flush=True)
    
    return no_certified, total_images, certified

# TODO: can we maybe spare no_classes?
def eval_certified(model, data_loader, n_classes=10, eps=.3, test_samples=np.inf, method='IBP'):
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    model.eval()
    certified = 0
    total_images = 0

    if method == "CROWN":
        certified, total_images = eval_crown(model, eps, data_loader, n_classes, test_samples, device)
    elif method == 'IBP':
        certified, total_images = eval_ibp(model, eps, data_loader, n_classes, test_samples, device)
    elif method == 'CROWN-IBP':
        certified, total_images = eval_crown_ibp(model, eps, data_loader, n_classes, test_samples, device)
    elif method == 'ADAPTIVE':
        certified, total_images, cert_results = eval_adaptive(model, eps, data_loader, n_classes, test_samples, device)
    elif isinstance(method, list):
        certified, total_images, cert_results = eval_adaptive(model, eps, data_loader, n_classes, test_samples, device, methods=method)
    elif method == 'COMPLETE':
        # TODO: Infer input shape or pass it, pass timeout and no_cores!
        eval_complete_abcrown(model, eps, data_loader, n_classes, input_shape=(1, 28, 28), test_samples=test_samples, timeout=1000, no_cores=28, device=device)
    elif isinstance(method, (list, tuple, np.ndarray)):
        certified, total_images, cert_results = eval_adaptive(model, eps, data_loader, n_classes, test_samples, device, methods=method)
    else:
        assert False, "UNKNOWN BOUNDING METHOD!"
    
    # print(f"Certified accuracy on test examples for eps {eps}: {certified / total_images}")
    return (certified / total_images).cpu().item() if torch.is_tensor(certified) else certified / total_images

# TODO: Make PGD params adjustable
def eval_adversarial(model, data_loader, eps, n_classes=10, device='cuda', test_samples=np.inf, return_adv_indices=False):
    model.eval()
    adv_preds = np.array([])
    labels = np.array([])
    data_min = data_loader.min.to(device)
    data_max = data_loader.max.to(device)
    
    for batch_idx, (data, targets) in tqdm(enumerate(data_loader)):
        if len(labels) >= test_samples:
            break
        
        batch_indices = min(len(targets), test_samples - len(labels))
        data = data[:batch_indices]
        targets = targets[:batch_indices]
        
        data, targets = data.to(device), targets.to(device)
        eps = eps.to(device)

        x_test_adv = pgd_attack(
            model=model,
            data=data,
            target=targets,
            x_L=torch.clamp(data - eps, data_min, data_max).to(device), 
            x_U=torch.clamp(data + eps, data_min, data_max).to(device),
            restarts=5,
            step_size=.1,
            n_steps=40,
            early_stopping=False,
            device=device
        )
        
        adv_predictions_batch = model(x_test_adv)
        adv_predictions_batch = torch.argmax(adv_predictions_batch, dim=1).cpu().numpy()
        if len(labels) + len(targets) > test_samples:
            too_many_samples_no = (len(labels) + len(targets)) % test_samples
            adv_predictions_batch = adv_predictions_batch[:-too_many_samples_no]
            targets = targets[:-too_many_samples_no]

        adv_preds = np.append(adv_preds, adv_predictions_batch)
        labels = np.append(labels, targets.cpu())

    test_samples = min(test_samples, len(labels))

    adv_accuracy = accuracy_score(labels, adv_preds)
    
    if return_adv_indices:
        adv_sample_found = labels != adv_preds
        return adv_accuracy, adv_sample_found
    # print(f"Accuracy on adversarial test examples for eps {eps}: {adv_accuracy}")
    return adv_accuracy

def eval_model(model, data_loader, n_classes=10, eps=.3, test_samples=np.inf, method='ADAPTIVE', device='cuda'):
    std_acc = eval_acc(model, test_loader=data_loader, test_samples=test_samples)
    cert_acc = eval_certified(model=model, data_loader=data_loader, n_classes=n_classes, eps=eps, test_samples=test_samples, method=method)
    adv_acc = eval_adversarial(model=model, data_loader=data_loader, n_classes=n_classes, eps=eps, device=device, test_samples=test_samples)
    
    return std_acc, cert_acc, adv_acc
    
def eval_epoch(model, data_loader, eps, n_classes, device='cuda', test_samples=1000, verification_method="IBP", results_path="./results"):
    os.makedirs(results_path, exist_ok=True)
    model.eval()
    std_acc = eval_acc(model, test_loader=data_loader, test_samples=test_samples)
    if (eps == 0.).all():
        cert_acc = adv_acc = std_acc
    else:
        with torch.no_grad():
            cert_acc = eval_certified(model=model, data_loader=data_loader, n_classes=n_classes, eps=eps, test_samples=test_samples, method=verification_method)
            adv_acc = eval_adversarial(model=model, data_loader=data_loader, n_classes=n_classes, eps=eps, device=device, test_samples=test_samples)
    
    with open(f"{results_path}/stats.json", "w") as f:
        json.dump(
            {"acc": std_acc, "cert_acc": cert_acc, "adv_acc": adv_acc}, f
        )
    model.train()

    return std_acc, cert_acc, adv_acc 
    
