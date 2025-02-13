import sys

import numpy as np

import sparse_transform.asmt.asmt as asmt
import sparse_transform.asmt.fasmt_parallel as fasmt
from sparse_transform.smt.random_group_testing import decode, decode_robust
from sparse_transform.qsft.signals.synthetic_signal import get_random_signal

import colorama
from scipy.special import binom

if __name__ == '__main__':
    # np.random.seed(8)  # Make it reproducible
    q = 2  # Aspirational
    parameter_set = 1  # Choose which set of parameters to use (See options below)

    if parameter_set == 1:  # Noiseless Low-Degree
        n = 500
        b_asmt = 200  # for ASMT
        b_fasmt = 12  # for Batched FASMT
        sparsity = 100
        a_min = 1
        a_max = 2
        noise_sd = 0
        t = 10  # only for generating the signal
        noise_model = None
    elif parameter_set == 2:  # Noiseless Low-Degree SIMPLE
        n = 20
        b_asmt = 30  # for ASMT
        b_fasmt = 2  # for Batched FASMT
        sparsity = 3
        a_min = 1
        a_max = 2
        noise_sd = 0
        t = 3  # only for generating the signal
        noise_model = None
    else:
        raise NotImplementedError
    '''
    Generate a Signal Object
    '''
    test_signal = get_random_signal(n=n,
                                    sparsity=sparsity,
                                    a_min=a_min,
                                    a_max=a_max,
                                    noise_sd=noise_sd,
                                    max_weight=t,
                                    noise_model=noise_model)

    algos = [
        {"algo": asmt, "transform_args": {"query_method": "simple"}, "label": "ASMT (Wendler)"},
        {"algo": asmt, "transform_args": {"query_method": "group_testing", "b": b_asmt, "wt": 0.9, "t": t, "decoder": decode}, "label": "ASMT"},
        {"algo": fasmt, "transform_args": {"query_method": "group_testing", "decoder": decode}, "label": "FASMT"},
        {"algo": fasmt, "transform_args": {"query_method": "group_testing", "decoder": decode, "b": b_fasmt},
         "label": "Batched FASMT"},
    ]

    '''
    Create instances of each algorithm and perform the transformation
    '''
    for algo_specs in algos:
        sys.stderr.flush()
        sys.stdout.flush()
        print(f'{colorama.Fore.RED}---------------------------------------------\nRunning Tests with {algo_specs}{colorama.Fore.RESET}')

        algo_instance = algo_specs["algo"]()
        result = algo_instance.transform(test_signal, verbosity=5, timing_verbose=True, report=True, sort=True, **algo_specs["transform_args"])

        '''
        Display the Reported Results
        '''
        transform = result.get("transform")
        loc = result.get("locations")
        n_used = result.get("n_samples")
        n_batches = result.get("n_batches")
        peeled = result.get("locations")
        avg_hamming_weight = result.get("avg_hamming_weight")
        max_hamming_weight = result.get("max_hamming_weight")

        runtime = result.get('runtime')
        sampling_time = result.get('sampling_time')

        def color_sign(x):
            c = colorama.Fore.RED if x > 0 else colorama.Fore.RESET
            return f'{c}{x}{colorama.Fore.RESET}'

        sys.stderr.flush()
        sys.stdout.flush()
        np.set_printoptions(formatter={'int': color_sign}, threshold=1000, linewidth=1000, edgeitems=5)

        print("found non-zero indices QSFT: ")
        print(peeled)
        print("True non-zero indices: ")
        print(test_signal.loc.T)

        # reset the print options
        np.set_printoptions()

        print("Total samples = ", n_used)
        print("Total sample ratio = ", n_used / q ** n)
        print("Total numder of batches = ", n_batches)
        # print(f"Information theoretic sample lower bound (worst case) = {int(np.ceil(sparsity * np.log(binom(n, t)) / np.log(sparsity + 1)))}")

        signal_w_diff = test_signal.signal_w.copy()
        for key in transform.keys():
            signal_w_diff[key] = signal_w_diff.get(key, 0) - transform[key]
        print(f"NMSE = {np.sum(np.abs(list(signal_w_diff.values())) ** 2) / np.sum(np.abs(list(test_signal.signal_w.values())) ** 2)}")
        print("AVG Hamming Weight of Nonzero Locations = ", avg_hamming_weight)
        print("Max Hamming Weight of Nonzero Locations = ", max_hamming_weight)

        print(f"Total Runtime = {runtime}, Sampling Time = {sampling_time}")
