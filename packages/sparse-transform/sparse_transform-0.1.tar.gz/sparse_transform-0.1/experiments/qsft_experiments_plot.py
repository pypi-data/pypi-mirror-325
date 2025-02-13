from sparse_transform.qsft.utils.query import get_bch_decoder
from sparse_transform.qsft.signals.synthetic_signal import get_random_subsampled_signal
import numpy as np
from collections import Counter
import logging
import matplotlib.pyplot as plt
from multiprocess import Pool
import itertools
import pickle
logger = logging.getLogger(__name__)


def run(iter=(0, 0, 0),
        t=None,
        b=None,
        n=None,
        max_weight=None,
        sparsity=None,
        p=None,
        peeling_method=None,
        refined=None,
        regress=None,
        res_energy_cutoff=0.5,
        chase_depth=None,
        trap_exit=False,
        peel_average=None,
        probabalistic_peel=None,
        dectype='soft'):
    qsft_args = {
        "num_subsample": 3,
        "num_repeat": 1,
        "reconstruct_method_source": "coded",
        "reconstruct_method_channel": "identity-siso",
        "b": b,
        "source_decoder": get_bch_decoder(n, t, dectype=dectype, chase_depth=chase_depth)
    }
    query_args = {
        "query_method": "complex",
        "num_subsample": 3,
        "delays_method_source": "joint-coded",
        "subsampling_method": "qsft",
        "delays_method_channel": "identity-siso",
        "num_repeat": 1,
        "b": b,
        "t": t
    }
    verbosity = 0
    test_signal = get_random_subsampled_signal(n=n, q=2, noise_sd=0, sparsity=sparsity, a_min=1, a_max=10,
                                               query_args=query_args, max_weight=max_weight, skewed=p)
    logger.info(f"Skew={p}")
    import sparse_transform.qsft as sft
    if peeling_method == "single-detect":
        noise_sd_space = np.linspace(0.1, 1, 20)
        best_peeled = 0
        for noise_sd in noise_sd_space:
            trial_result = sft.transform(test_signal,
                                         verbosity=verbosity,
                                         timing_verbose=True,
                                         report=True,
                                         sort=True,
                                         noise_sd=noise_sd,
                                         refined=refined,
                                         **qsft_args,
                                         peeling_method=peeling_method,
                                         regress=regress)
            if len(trial_result.get("locations")) >= best_peeled:
                result = trial_result
    elif peeling_method == "multi-detect":
        result = sft.transform(test_signal,
                               verbosity=verbosity,
                               timing_verbose=True,
                               report=True,
                               sort=True,
                               noise_sd=0,
                               refined=refined,
                               **qsft_args,
                               peeling_method=peeling_method,
                               regress=regress,
                               res_energy_cutoff=res_energy_cutoff,
                               trap_exit=trap_exit,
                               peel_average=peel_average,
                               probabalistic_peel=probabalistic_peel,)

    gwht = result.get("transform")
    loc = result.get("locations")
    n_used = result.get("n_samples")
    peeled = result.get("locations")
    avg_hamming_weight = result.get("avg_hamming_weight")
    max_hamming_weight = result.get("max_hamming_weight")
    matching = 0
    loc_dict = Counter([tuple(c) for c in test_signal.locq.T])
    for c in peeled:
        matching += tuple(c) in loc_dict
    signal_w_diff = test_signal.signal_w.copy()
    for key in gwht.keys():
        signal_w_diff[key] = signal_w_diff.get(key, 0) - gwht[key]
    nmse = np.sum(np.abs(list(signal_w_diff.values())) ** 2) / np.sum(np.abs(list(test_signal.signal_w.values())) ** 2)
    print(f"Runtime: {result['runtime']}")
    return min(1, nmse), matching, iter


def gen_data(configs, signal_configs, n_mc=10, n_p=5, parallel=False, pspace=None):
    if pspace is None:
        pspace = np.linspace(0.1, 2, n_p)
    errors = np.zeros(shape=(n_p, n_mc, len(configs)))
    n_dec = np.zeros(shape=(n_p, n_mc, len(configs)))
    iterations = itertools.product(range(n_p), range(len(configs)), range(n_mc))
    run_func = lambda x: run(**configs[x[1]], **signal_configs[x[1]], p=pspace[x[0]], iter=x)
    if parallel:
        p = Pool(2)
        pool_res = list(p.map(run_func, iterations))
    else:
        pool_res = list(map(run_func, iterations))
    for result in pool_res:
        i_p, i_c, i_mc = result[-1]
        errors[i_p, i_mc, i_c] = result[0]
        n_dec[i_p, i_mc, i_c] = result[1]
    res = np.mean(errors, 1)
    n_dec_res = np.mean(n_dec, 1)
    return pspace, res, n_dec_res


def make_plot(pspace=None, n_err=None, n_dec=None, labels=None, linspecs=None, configs=None, signal_configs=None):
    for i in range(len(labels)):
        plt.semilogy(pspace, n_err[:, i], linspecs[i], label=labels[i])
    plt.grid(which='major')
    plt.minorticks_on()
    plt.grid(which='minor')
    plt.xlabel("p")
    plt.ylabel("NMSE")
    plt.legend()
    plt.axis([0, pspace[-1]+0.1, 1e-3, 1.5])
    plt.show()
    # TODO: Fix bits per symbol plot
    for i in range(len(labels)):
        plt.plot(pspace, n_dec[:, i]*3*np.log2(100)/1584, linspecs[i], label=labels[i])
    plt.xlabel("p")
    plt.ylabel("bits per symbol")
    plt.legend()
    plt.show()
    print(n_dec)


def make_plot_from_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    make_plot(**data)


def run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config.pickle', pspace=None):
    pspace, n_err, n_dec = gen_data(configs, signal_configs, n_mc=n_mc, n_p=n_p, pspace=pspace)
    data_results = {'pspace': pspace, 'n_err': n_err, 'n_dec': n_dec, "labels": labels, "linspecs": linspecs,
                    "configs": configs, "signal_configs": signal_configs}
    with open(filename, 'wb') as file:
        pickle.dump(data_results, file)
    make_plot(**data_results)


def runtime_comparison(max_weight, p, n, b, t, sparsity, dectype, chase_depth, order):
    qsft_args = {
        "num_subsample": 3,
        "num_repeat": 1,
        "reconstruct_method_source": "coded",
        "reconstruct_method_channel": "identity-siso",
        "b": b,
        "source_decoder": get_bch_decoder(n, t, dectype=dectype, chase_depth=chase_depth)
    }
    query_args = {
        "query_method": "complex",
        "num_subsample": 3,
        "delays_method_source": "joint-coded",
        "subsampling_method": "qsft",
        "delays_method_channel": "identity-siso",
        "num_repeat": 1,
        "b": b,
        "t": t
    }
    verbosity = 0
    test_signal = get_random_subsampled_signal(n=n, q=2, noise_sd=0, sparsity=sparsity, a_min=1, a_max=10,
                                               query_args=query_args, max_weight=max_weight, skewed=p)
    import sparse_transform.qsft as sft
    result1 = sft.transform(test_signal,
                           verbosity=verbosity,
                           timing_verbose=True,
                           report=True,
                           sort=True,
                           noise_sd=0,
                           refined=False,
                           **qsft_args,
                           peeling_method='multi-detect',
                           res_energy_cutoff=0.9,
                           trap_exit=False,
                           peel_average=True,
                           probabalistic_peel=False,)
    result2 = sft.transform_via_omp(test_signal, b=b, order=order)
    out1  = extract_runtime_nmse_samples(result1, test_signal)
    out2  = extract_runtime_nmse_samples(result2, test_signal)
    return out1, out2

def extract_runtime_nmse_samples(result, signal):
    gwht = result.get("transform")
    n_used = result.get("n_samples")
    peeled = result.get("locations")
    matching = 0
    loc_dict = Counter([tuple(c) for c in signal.locq.T])
    for c in peeled:
        matching += tuple(c) in loc_dict
    signal_w_diff = signal.signal_w.copy()
    for key in gwht.keys():
        signal_w_diff[key] = signal_w_diff.get(key, 0) - gwht[key]
    signal_w_diff = signal.signal_w.copy()
    for key in gwht.keys():
        signal_w_diff[key] = signal_w_diff.get(key, 0) - gwht[key]
    nmse = np.sum(np.abs(list(signal_w_diff.values())) ** 2) / np.sum(np.abs(list(signal.signal_w.values())) ** 2)
    print(f"Runtime: {result['runtime']}")
    return min(1, nmse), matching, n_used


if __name__ == '__main__':
    logging.basicConfig(filename='qsft_plots.log', level=logging.INFO)
    logger.info('Started')
    np.random.seed(0)

    exp1 = False
    exp2 = False
    exp3 = False
    exp4 = False
    exp5 = False
    exp6 = False
    exp7 = True
    if exp1:
        n = 100
        b = 4
        t = 4
        sparsity = 100
        configs = [{'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.2, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.5, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.7, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"}]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['cutoff = 0.2', 'cutoff = 0.5', 'cutoff = 0.7', 'cutoff = 0.9']
        linspecs = ['k-o', 'g--^', 'b--*', 'r-.']
        run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config1.pickle',
                   pspace=np.linspace(0.1, 1.4, 5))

    if exp2:
        n = 100
        sparsity = 200
        configs = [{'t': 4, 'b': 4, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 4, 'dectype': "subseq-soft-t2"},
                   {'t': 8, 'b': 4, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 8, 'dectype': "subseq-soft-t2"},
                   {'t': 12, 'b': 4, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 12, 'dectype': "subseq-soft-t2"},
                   {'t': 16, 'b': 4, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 16, 'dectype': "subseq-soft-t2"},
                   {'t': 4, 'b': 5, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 4, 'dectype': "subseq-soft-t2"},
                   {'t': 8, 'b': 5, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 8, 'dectype': "subseq-soft-t2"},]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['t=4, b=4', 't=8, b=4', 't=12, b=4', 't=16, b=4', 't=4, b=5', 't=8, b=5']
        linspecs = ['k-o', 'k--^', 'k--*', 'k-.', 'r-o', 'r--^']
        run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config2.pickle',
                   pspace=np.linspace(0.1, 1.4, 5))

    if exp3:
        n = 100
        sparsity = 100
        t = 4
        b = 4
        configs = [{'t': t, 'b': b, 'peeling_method': "single-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": t},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "ml-soft-t2"},
                   ]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['single-detect', 'multi-detect-subseq', 'multi-detect-ml',]
        linspecs = ['r-o', 'g-o', 'b-o']
        run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config3.pickle',
                   pspace=np.linspace(0.1, 1.4, 5))

    if exp4:
        n = 100
        sparsity = 100
        t = 4
        b = 4
        configs = [{'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 2 * t, 'dectype': "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'res_energy_cutoff': 0.9, "chase_depth": 1 * t, 'dectype': "subseq-soft-t2-opt"},
                   ]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['chase-3', 'chase-2', 'chase-1']
        linspecs = ['r-o', 'g-o', 'b-o']
        run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config4.pickle',
                   pspace=np.linspace(0.1, 1.4, 5))

    if exp5:
        n = 100
        sparsity = 100
        t = 4
        b = 4
        configs = [{'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'linear',
                    'peel_average': True, 'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype':
                        "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': None,
                    'peel_average': True, 'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype':
                        "subseq-soft-t2-opt"},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': 'freq_domain',
                    'peel_average': True, 'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype':
                        "subseq-soft-t2-opt"}
                   ]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['regress-time', 'regress-False', 'regress-freq']
        linspecs = ['r-o', 'g-o', 'b-o']
        run_config(configs, signal_configs, labels, linspecs, n_mc=30, n_p=5, filename='config5.pickle',
                   pspace=np.linspace(0.1, 0.8, 5))

    if exp6:
        n = 100
        sparsity = 100
        t = 4
        b = 4
        configs = [{'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': None,
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt",
                    'peel_average': True, 'probabalistic_peel': True,},
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': None,
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt",
                    'peel_average': False, 'probabalistic_peel': True, },
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': None,
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt",
                    'peel_average': True, 'probabalistic_peel': False, },
                   {'t': t, 'b': b, 'peeling_method': "multi-detect", 'refined': False, 'regress': None,
                    'res_energy_cutoff': 0.9, "chase_depth": 3 * t, 'dectype': "subseq-soft-t2-opt",
                    'peel_average': False, 'probabalistic_peel': False, },
                   ]
        signal_configs = [{'n': n, 'max_weight': 3, 'sparsity': sparsity}] * len(configs)
        labels = ['avg-prob', 'prob', 'avg', 'none']
        linspecs = ['r-o', 'g-o', 'b-o', 'k-o']
        run_config(configs, signal_configs, labels, linspecs, n_mc=10, n_p=5, filename='config6.pickle',
                   pspace=np.linspace(0.1, 1, 5))

    if exp7:
        n = 100
        sparsity = 100
        t = 4
        b = 5
        res = runtime_comparison(max_weight=3,
                               p=0.6,
                               n=n,
                               b=b,
                               t=t,
                               sparsity=sparsity,
                               dectype='subseq-soft-t2-opt',
                               chase_depth= 3 * t,
                               order = 3)
        breakpoint()
    logger.info('Finished')
