import torch
import os
import random
import numpy as np

def export_onnx(model, file_name, batch_size, input_shape):
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
        # Input to the model
    if len(input_shape) == 4:
        batch_size = input_shape[0]
        input_shape = input_shape[1:4]
    x = torch.randn(batch_size, *input_shape, requires_grad=True).to(device)
    torch_out = model(x)

    # Export the model
    torch.onnx.export(model,               # model being run
                    x,                         # model input (or a tuple for multiple inputs)
                    file_name,   # where to save the model (can be a file or file-like object)
                    export_params=True,        # store the trained parameter weights inside the model file
                    opset_version=10,          # the ONNX version to export the model to
                    do_constant_folding=False,  # whether to execute constant folding for optimization
                    input_names = ['input'],   # the model's input names
                    output_names = ['output'], # the model's output names
                    dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                                    'output' : {0 : 'batch_size'}})
    
def save_checkpoint(model, optimizer, loss, epoch, results_path):
    if os.path.exists(f"{results_path}/{epoch}_checkpoint.pt"):
        assert False, "Checkpoint already exists!"
    torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss,
            }, f"{results_path}/{epoch}_checkpoint.pt")

def construct_c(data, target, n_classes):
    c = torch.eye(n_classes).type_as(data)[target].unsqueeze(1) - torch.eye(n_classes).type_as(data).unsqueeze(0)
    # remove specifications to self
    I = (~(target.data.unsqueeze(1) == torch.arange(n_classes).type_as(target.data).unsqueeze(0)))
    c = (c[I].view(data.size(0), n_classes - 1, n_classes))
    return c

def seed_ctrain(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False