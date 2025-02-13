from pathlib import Path
from tqdm import tqdm
import numpy as np
import time
from sparse_transform.qsft.signals.input_signal_subsampled import SubsampledSignal
from sparse_transform.qsft.utils.general import load_data, save_data

class OddSubsampledSignal(SubsampledSignal):
    """
    A shell Class for input signal/functions that are too large and cannot be stored in their entirety. In addition to
    the signal itself, this must also contain information about the M and D matricies that are used for subsampling
    Notable attributes are included below.

    Attributes
    ---------
    query_args : dict
    These are the parameters that determine the structure of the Ms and Ds needed for subsampling.
    It contains the following sub-parameters:
        b : int
        The max dimension of subsampling (i.e., we will subsample functions with b inputs, or equivalently a signal of
        length q^b)
        all_bs : list, (optional)
        List of all the b values that should be subsampled. This is most useful when you want to repeat an experiment
        many times with different values of b to see which is most efficient
        For a description of the "delays_method_channel", "delays_method_source", "num_repeat" and "num_subsample", see
        the docstring of the QSFT class.
        subsampling_method
            If set to "simple" the M matricies are generated according to the construction in Appendix C, i.e., a
            block-wise identity structure.
            If set to "complex" the elements of the M matricies are uniformly populated from integers from 0 to q-1.
            It should be noted that these matricies are not checked to be full rank (w.r.t. the module where arithemtic is
            over the integer quotient ring), and so it is possible that the actual dimension of subsampling may be
            lower. For large enough n and b this isn't a problem, since w.h.p. the matricies are full rank.

    L : np.array
    An array that enumerates all q^b q-ary vectors of length b

    foldername : str
    If set, and the file {foldername}/Ms_and_Ds.pickle exists, the Ms and Ds are read directly from the file.
    Furthermore, if the transforms for all the bs are in {foldername}/transforms/U{i}_b{b}.pickle, the transforms can be
    directly loaded into memory.
    """

    def _subsample_qsft(self):
        """
        Subsamples and computes the sparse fourier transform for each subsampling group if the samples are not already
        present in the folder
        """
        self.Us = [[{} for j in range(len(self.Ds[i]))] for i in range(len(self.Ms))]
        self.transformTimes = [[{} for j in range(len(self.Ds[i]))] for i in range(len(self.Ms))]

        if self.foldername:
            Path(f"{self.foldername}/samples").mkdir(exist_ok=True)
            Path(f"{self.foldername}/transforms/").mkdir(exist_ok=True)

        pbar = tqdm(total=0, position=0)
        for i in range(len(self.Ms)):
            for j in range(len(self.Ds[i])):
                transform_file = Path(f"{self.foldername}/transforms/U{i}_{j}.pickle")
                if self.foldername and transform_file.is_file():
                    self.Us[i][j], self.transformTimes[i][j] = load_data(transform_file)
                    pbar.total = len(self.Ms) * len(self.Ds[0]) * len(self.Us[i][j])
                    pbar.update(len(self.Us[i][j]))
                else:
                    sample_file = Path(f"{self.foldername}/samples/M{i}_D{j}.pickle")
                    if self.foldername and sample_file.is_file():
                        samples = load_data(sample_file)
                        pbar.total = len(self.Ms) * len(self.Ds[0]) * len(samples)
                        pbar.update(len(samples))
                    else:
                        query_indices = self._get_qsft_query_indices(self.Ms[i], self.Ds[i][j], dec=False)
                        block_length = len(query_indices[0])
                        samples = np.zeros((len(query_indices), block_length), dtype=complex)
                        pbar.total = len(self.Ms) * len(self.Ds[0]) * len(query_indices)
                        if block_length > 10000:
                            for k in range(len(query_indices)):
                                samples[k] = self.subsample(query_indices[k])
                                pbar.update()
                        else:
                            all_query_indices = np.concatenate(query_indices)
                            all_samples = self.subsample(all_query_indices)
                            for k in range(len(query_indices)):
                                samples[k] = all_samples[k * block_length: (k+1) * block_length]
                                pbar.update()
                        if self.foldername:
                            save_data(samples, sample_file)
                    for b in self.all_bs:
                        start_time = time.time()
                        self.Us[i][j][b] = self._compute_subtransform(samples, b)
                        self.transformTimes[i][j][b] = time.time() - start_time
                    if self.foldername:
                        save_data((self.Us[i][j], self.transformTimes[i][j]), transform_file)
