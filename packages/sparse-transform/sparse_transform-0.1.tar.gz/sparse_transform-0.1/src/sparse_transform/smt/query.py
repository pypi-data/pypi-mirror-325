'''
Methods for the query generator: specifically, to

1. generate sparsity coefficients b and subsampling matrices M
2. get the indices of a signal subsample
3. compute a subsampled and delayed Walsh-Hadamard transform.
'''
import time
import numpy as np
from sparse_transform.smt.utils import  bin_to_dec, binary_ints
from sparse_transform.smt.random_group_testing import get_random_near_const_weight_mtrx, get_gt_delay_matrix
import logging

logger = logging.getLogger(__name__)


def get_Ms_simple(n, b, q, num_to_get=None, **kwargs):
    '''
    Sets Ms[0] = [I 0 ...], Ms[1] = [0 I ...], Ms[2] = [0 0 I 0 ...] and so forth. See get_Ms for full signature.
    '''
    Ms = []
    for i in range(num_to_get - 1, -1, -1):
        M = np.zeros((n, b), dtype=int32)
        M[(b * i) : (b * (i + 1)), :] = np.eye(b)
        Ms.append(M)
    return Ms


def get_Ms_random(n, b, q, num_to_get=None, **kwargs):
    """
    Generate M uniformly at random.
    #TODO This should probably do something else
    """
    Ms = []
    # TODO Prevent duplicate M (Not a problem for large n, m )
    for i in range(num_to_get):
        M = np.random.randint(q, size=(n, b))
        Ms.append(M)
    return Ms

"""
You need to pass both m and wt for now. I think you should choose m such that m is as small as it can be
while still having good performance
"""
def get_Ms_gt(n, b, q=2, num_to_get=None, **kwargs):
    wt = kwargs.get("wt")
    m = kwargs.get("p")
    t = kwargs.get("t")
    Ms = []
    for i in range(num_to_get):
        M = get_random_near_const_weight_mtrx(n, m, int(wt*m/t))[:b].T
        Ms.append(M)
    return Ms

def get_Ms(n, b, q, num_to_get=None, method="simple", **kwargs):
    '''
    Gets subsampling matrices for different sparsity levels.

    Arguments
    ---------
    n : int
    log_q of the signal length (number of inputs to function).

    b : int
    subsampling dimension.

    num_to_get : int
    The number of M matrices to return.

    method : str
    The method to use. All methods referenced must use this signature (minus "method".)

    Returns
    -------
    Ms : list of numpy.ndarrays, shape (n, b)
    The list of subsampling matrices.
    '''
    if num_to_get is None:
        num_to_get = max(n // b, 3)

    if method == "simple" and num_to_get > n // b:
        raise ValueError("When query_method is 'simple', the number of M matrices to return cannot be larger than n // b")

    return {
        "simple": get_Ms_simple,
        "random": get_Ms_random,
        "group_testing": get_Ms_gt,
    }.get(method)(n, b, q, num_to_get, **kwargs)


def get_D_identity(n, **kwargs):
    int_delays = np.zeros(n, )
    int_delays = np.vstack((int_delays, np.eye(n)))
    return int_delays.astype(int)


def get_D_random(n, **kwargs):
    '''
    Gets a random delays matrix of dimension (num_delays, n). See get_D for full signature.
    '''
    q=kwargs.get("q")
    num_delays = kwargs.get("num_delays")
    return np.random.choice(q, (num_delays, n))


def get_D_source_coded(n, **kwargs):
    wt = kwargs.get("wt")
    p = kwargs.get("p")
    t = kwargs.get("t")
    D = get_gt_delay_matrix(n, p, wt, t, "const_col")  # TODO maybe add an option to allow bernoulli?
    return np.array(D, dtype=int)


def get_D_nso(n, D_source, **kwargs):
    '''
    Get a repetition code based (NSO-SPRIGHT) delays matrix. See get_D for full signature.
    '''
    num_repeat = kwargs.get("num_repeat")
    q = kwargs.get("q")
    random_offsets = get_D_random(n, q=q, num_delays=num_repeat)
    D = []
    for row in random_offsets:
        modulated_offsets = (row - D_source) % q
        D.append(modulated_offsets)
    return D


def get_D_channel_coded(n, D, **kwargs):
    raise NotImplementedError("One day this might be implemented")

def get_D_channel_identity(n, D, **kwargs):
    q = kwargs.get("q")
    return [D % q]

def get_D(n, **kwargs):
    '''
    Delay generator: gets a delays matrix.

    Arguments
    ---------
    n : int
    number of bits: log2 of the signal length.

    Returns
    -------
    D : numpy.ndarray of binary ints, dimension (num_delays, n).
    The delays matrix; if num_delays is not specified in kwargs, see the relevant sub-function for a default.
    '''
    delays_method_source = kwargs.get("delays_method_source", "random")
    D = {
        "random": get_D_random,
        "identity": get_D_identity,
        "coded": get_D_source_coded
    }.get(delays_method_source)(n, **kwargs)

    delays_method_channel = kwargs.get("delays_method_channel", "identity")
    D = {  # TODO As currently implemented 'nso' and 'identity' should do the same thing, but this could change
            "nso": get_D_channel_identity,
            "coded": get_D_channel_coded,
            "identity": get_D_channel_identity
    }.get(delays_method_channel)(n, D, **kwargs)
    return D


def subsample_indices(M, d):
    '''
    Query generator: creates indices for signal subsamples.

    Arguments
    ---------
    M : numpy.ndarray, shape (n, b)
    The subsampling matrix; takes on binary values.

    d : numpy.ndarray, shape (n,)
    The subsampling offset; takes on binary values.

    Returns
    -------
    indices : numpy.ndarray, shape (B,)
    The (decimal) subsample indices. Mostly for debugging purposes.
    '''
    L = binary_ints(M.shape[1])
    inds_binary = np.mod(np.dot(M, L).T + d, 2).T
    return bin_to_dec(inds_binary)


def get_Ms_and_Ds(n, q, **kwargs):
    """
    Based on the parameters provided in kwargs, generates Ms and Ds.
    """
    timing_verbose = kwargs.get("timing_verbose", False)
    if timing_verbose:
        start_time = time.time()
    query_method = kwargs.get("query_method")
    if query_method == "group_testing":
        logger.info("Query Method is set to group testing. Ensure that wt and p are set correctly!")
        logger.info(f"Current parameters: wt={kwargs.get('wt')}, p={kwargs.get('p')}")
    b = kwargs.get("b")
    num_subsample = kwargs.get("num_subsample")
    p = kwargs.get("p")
    wt = kwargs.get("wt")
    t = kwargs.get("t")
    ms_args = dict(p=p, wt=wt, t=t)
    Ms = get_Ms(n, b, q, method=query_method, num_to_get=num_subsample, **ms_args)
    if timing_verbose:
        logger.info(f"M Generation:{time.time() - start_time}")
    Ds = []
    if timing_verbose:
        start_time = time.time()
    D = get_D(n, q=q, **kwargs)
    if timing_verbose:
        logger.info(f"D Generation:{time.time() - start_time}")
    for _ in Ms:
        Ds.append(D)
    return Ms, Ds

