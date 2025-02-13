'''
Class that perfroms noise search by running repeated tests
'''
import numpy as np
import logging
from sparse_transform.qsft.signals.input_signal_subsampled import SubsampledSignal as FourierSubsampledSignal
from sparse_transform.smt.input_signal_subsampled import SubsampledSignal as MobiusSubsampledSignal

logger = logging.getLogger(__name__)


class NoiseEstimator:
    '''
    Class to estimate peeling noise

    Attributes
    ---------
    n, q: int, they define the problem
    sft: QSFT object that we can use to peel 
    transform_args: dictionary required to run tests
    query_args: distionary required to run tests
    func: the oracle, required to run tests
    signal: the signal object, required to run tests. 
    '''

    def __init__(self, algo, n, q, transform_args, query_args, train_signal, test_signal) -> None:
        # signal parameters:
        self.n = n
        self.q = q
        self.algo = algo
        self.transform_args = transform_args
        self.query_args = query_args
        self.train_signal = train_signal
        self.test_signal = test_signal

        # algorithm parameters:
        # initialize log noise level
        self.log_init = -5
        # max number of iterations to find the search interval (first phase)
        self.iter_1 = 10
        # max number of iterations to find the best value within the search interval (second phase)
        self.iter_2 = 20
        # counter is in relation to iter_2
        self.counter_2 = 0
        # log10 step size during the first phase
        self.step = 1
        # minimal distance between left and right before we call it a stop
        self.min_dist = 0.1
        # ratio is golden ratio
        self.ratio = (np.sqrt(5) + 1) / 2
        # This is the threshold of NMSE I want. If at some point I see that NMSe is less than this number,I'm done.
        self.threshold = 0.001
        # cache for test results
        self.cache = {}

    def estimate_noise(self):
        """
        Find the best noise level for a given problem
        :return: float32
        """

        logger.info(f"Searching for the best value for noise_sd")

        left, right = self.find_gap()

        logger.info(f"Phase 1 resulted in noise interval: [{10 ** left}, {10 ** right}]")

        if left == right:
            logger.info(f"Phase 2 resulted in noise: {10 ** left}")
            return 10 ** left
        else:
            try:
                answer = self.find_noise(left, right)
                logger.info(f"Phase 2 resulted in noise: {10 ** answer}")
                return 10 ** answer
            except TimeoutError:
                return None

    # a function that simplifies running the test
    def _test_noise(self, log_noise):
        log_noise = round(log_noise, 3)
        if log_noise not in self.cache:
            self.transform_args["noise_sd"] = 10 ** log_noise
            result = self.algo(self.train_signal, verbosity=0, timing_verbose=False, report=True, sort=True, **self.transform_args)
            error, fail_low, fail_high = self._estimate_error(result["transform"]), result["fail_low_noise"], result["fail_high_noise"]
            self.cache[log_noise] = (error, fail_low, fail_high)
        return self.cache[log_noise]

    # a function that estimates the NMSE
    def _estimate_error(self, transform):
        if len(transform.keys()) == 0:
            return 1
        new_signal = self.test_signal.signal_t
        (sample_idx, samples) = list(new_signal.keys()), list(new_signal.values())
        batch_size = 10000

        y_hat = []
        for i in range(0, len(sample_idx), batch_size):
            sample_idx_batch = sample_idx[i:i + batch_size]
            if isinstance(self.test_signal, MobiusSubsampledSignal):
                y_hat.append(self._sample_mobius_function(transform, sample_idx_batch))
            elif isinstance(self.test_signal, FourierSubsampledSignal):
                y_hat.append(self._sample_fourier_function(transform, sample_idx_batch))
            else:
                raise ValueError

        y_hat = np.concatenate(y_hat)

        return np.linalg.norm(y_hat - samples) ** 2 / np.linalg.norm(samples) ** 2

    # This function finds the interval that the true noise lies in.
    def find_gap(self):

        left = None
        right = None
        log_noise = self.log_init
        for i in range(self.iter_1):

            # Run the test
            error, fail_low, fail_high = self._test_noise(log_noise)

            logger.info(f"Phase 1 Iteration {i} -- noise level: {10 ** log_noise}, nmse: {error}, fail_low: {fail_low}, fail_high: {fail_high}")

            if fail_high:
                right = log_noise

                if left is not None:
                    return [left, right]

                log_noise = log_noise - self.step
            elif fail_low:
                left = log_noise

                if right is not None:
                    return [left, right]

                log_noise = log_noise + self.step
            elif error <= self.threshold:
                return [log_noise, log_noise]
            else:
                if left is None:
                    log_noise = log_noise - self.step
                else:
                    log_noise = log_noise + self.step

        raise RuntimeError

    # Given an interval, this function helps finding the true noise. We do a golden search here.
    def find_noise(self, left, right) -> float:

        assert left < right

        self.counter_2 = self.counter_2 + 1
        if self.counter_2 >= self.iter_2:
            raise TimeoutError

        # Calculate the middles which is the goldren ratio whatever
        mid_1 = right - (right - left) / self.ratio
        mid_2 = left + (right - left) / self.ratio
        assert mid_1 < mid_2

        # evaluate on all four points
        test_points = [left, mid_1, mid_2, right]
        errors = []
        fail_left = []
        fail_right = []
        for tp in test_points:
            e, fl, fr = self._test_noise(tp)
            errors.append(e)
            fail_left.append(fl)
            fail_right.append(fr)

        # Determine if at any of these noises peeling is successful
        for i in range(3):
            if (errors[i]) <= self.threshold:
                self.answer_error = errors[i]
                return test_points[i]

        logger.info(f"Phase 2 Iteration {self.counter_2} -- noise interval: [{(10 ** test_points[0]):4f}, {(10 ** test_points[-1]):4f}]")

        # Terminate if left is too close to right
        if right - left < self.min_dist:
            self.answer = left
            self.answer_error = errors[0]
            return left

        # if it failed at middle points
        if fail_left[1]:
            return self.find_noise(mid_1, right)
        elif fail_right[1]:
            return self.find_noise(left, mid_1)
        elif fail_left[2]:
            return self.find_noise(mid_2, right)
        elif fail_right[2]:
            return self.find_noise(left, mid_2)
        else:  # no issues -- just compare mid points
            if errors[1] < errors[2]:
                return self.find_noise(left, mid_2)
            else:
                return self.find_noise(mid_1, right)

    def _sample_mobius_function(self, transform, sample_idx_batch):
        beta_keys = list(transform.keys())
        beta_values = list(transform.values())
        return ((1 - np.array(sample_idx_batch)) @ np.array(beta_keys).T < 0.5) @ np.array(beta_values)

    def _sample_fourier_function(self, transform, sample_idx_batch):
        beta_keys = list(transform.keys())
        beta_values = list(transform.values())
        freqs = np.array(sample_idx_batch) @ np.array(beta_keys).T
        H = np.exp(2j * np.pi * freqs / self.q)
        return H @ np.array(beta_values)
