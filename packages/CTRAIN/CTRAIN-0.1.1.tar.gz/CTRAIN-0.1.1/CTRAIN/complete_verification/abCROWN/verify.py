import json
import os
import time
import pickle
import subprocess
import traceback

import yaml

from CTRAIN.verification_systems.abCROWN.complete_verifier.abcrown import ABCROWN
from CTRAIN.verification_systems.abCROWN.complete_verifier.read_vnnlib import read_vnnlib
import torch
from CTRAIN.complete_verification.abCROWN.util import get_abcrown_standard_conf

MAX_LOSS = 10 ** 10

def limited_abcrown_eval(work_dir, runner_path='src/complete_verification/abCROWN/runner.py', *args, **kwargs):
    outer_timeout = kwargs['timeout'] * 1.2
    
    timestamp = time.time()
    
    args_pkl_path = f'{work_dir}/args_{timestamp}.pkl'
    result_path = f"{work_dir}/result_{timestamp}.pkl"
    
    with open(f'{work_dir}/args_{timestamp}.pkl', "wb") as f:
        pickle.dump((args, kwargs), f)
        
    verification_ok = False
    
    runner_args = [args_pkl_path, result_path]
    
    try:
        print(f"Running {['python3', runner_path] + runner_args}")
        process = subprocess.Popen(
            ["python3", runner_path] + runner_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        try:
            stdout, stderr = process.communicate(timeout=outer_timeout)
            print("Function finished successfully.")
            print("Output:", stdout.decode())
            print("Error Output:", stderr.decode())
            verification_ok = True

        except subprocess.TimeoutExpired:
            print(f"Function exceeded timeout of {outer_timeout} seconds. Terminating...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print("Function did not terminate after SIGTERM. Killing...")
                process.kill()

    except Exception as e:
        print(f"Error running the process: {e}")
    
    if verification_ok:
        with open(result_path, 'rb') as f:
            running_time, result = pickle.load(f)

        return running_time, result
    
    return MAX_LOSS, 'unknown'


def abcrown_eval(config, seed, instance, vnnlib_path='../../vnnlib/', model_name='mnist_6_100', model_path='./abCROWN/complete_verifier/models/eran/mnist_6_100_nat.pth', model_onnx_path=None, input_shape=[-1, 1, 28, 28], timeout=600, no_cores=28, par_factor=10):
    print(config, seed, instance)
    std_conf = config
    
    device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
    
    timestamp = time.time()
    
    std_conf['model']['name'] = model_name
    std_conf['model']['path'] = f'/tmp/{model_name}.pth' if model_name is not None else None
    std_conf['model']['onnx_path'] = model_onnx_path if model_onnx_path is not None else None
    std_conf['model']['input_shape'] = input_shape
    
    std_conf['general']['device'] = device
    
    std_conf['bab']['timeout'] = timeout
    
    if not std_conf['solver'].get('mip'):
        std_conf['solver']['mip'] = get_abcrown_standard_conf(timeout=timeout, no_cores=no_cores)['solver']['mip']
    std_conf['solver']['mip']['parallel_solvers'] = no_cores
    
    std_conf['specification']['vnnlib_path_prefix'] = vnnlib_path
    std_conf['specification']['vnnlib_path'] = instance
    std_conf['general']['output_file'] = f'/tmp/out_{timestamp}.pkl'
        
    print(json.dumps(config, indent=2))
    
    with open(f"/tmp/conf_{timestamp}.yaml", "w", encoding='u8') as f:
        yaml.dump(std_conf, f)
    
    abcrown_instance = ABCROWN(
        ['--config', f'/tmp/conf_{timestamp}.yaml']
    )
    
    # Precompile VNN-LIB s.t. each run can access the cache
    _ = read_vnnlib(instance)
    
    start_time = time.time()
    try:
        verification_res = abcrown_instance.main()
    except Exception as e:
        print(type(e), e)
        print(traceback.format_exc())
        return MAX_LOSS, 'unknown'
    end_time = time.time()
    
    os.system(f'rm /tmp/conf_{timestamp}.yaml')
    
    with open(f'/tmp/out_{timestamp}.pkl', 'rb') as f:
        result_dict = pickle.load(f)
    
    result = result_dict['results']
    
    if result == 'unknown':
        print("PENALISING RUNNING TIME DUE TO TIMEOUT!")
        running_time = timeout * par_factor if timeout > (end_time - start_time) else (end_time - start_time) * par_factor
    else:
        running_time = end_time - start_time
    
    return running_time, result

