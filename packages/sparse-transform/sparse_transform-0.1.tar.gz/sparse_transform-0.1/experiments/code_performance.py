import sys

import galois
import numpy as np
import matplotlib.pyplot as plt

from sparse_transform.qsft.utils.query import get_bch_decoder
from sparse_transform.qsft.codes.BCH import BCH


if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)

    n = 100
    t = 5
    bch = BCH(n, t)
    P = bch.get_delay_matrix()
    vec = np.zeros(n, dtype=int)
    vec[0] = 1
    vec[1] = 1
    vec[2] = 1
    vec = galois.GF2(vec)
    par = np.array(P[1:] @ vec)
    dec, n = bch.parity_decode(list(par))
    dec = np.array(dec[0, :], dtype=int)
    p1 = bch.get_parity_length()

    # Soft decoding test
    sigma = 0.7
    bpsk = (float(-1) ** par) + np.random.randn(len(par))*sigma/np.sqrt(2)
    dec3, n_err = bch.parity_decode_2chase(list(bpsk))
    dec3 = np.array(dec3[0, :], dtype=int)

    def correct(dec_test):
        return all(x == y for x,y in zip(dec_test, vec))

    # Plot the performance
    n_mc = 1000
    n_sig = 15
    rs_n_repeat = 4
    SNRs = np.logspace(-0.4, 0.8, n_sig)
    sigmas = np.linspace(0.5, 2, n_sig)
    dec_err = np.zeros(shape=(n_mc, n_sig, 2 + rs_n_repeat))
    for j, SNR in enumerate(SNRs):
        for i_mc in range(n_mc):
            s = np.sqrt(1/SNR)
            # generate signals
            bpsk_par = (float(-1) ** par) + np.random.randn(len(par))*s/np.sqrt(2)
            hard_par = (bpsk_par < 0).astype(int)

            # generate output
            dec1, n1 = bch.parity_decode(list(hard_par))
            dec2, n2 = bch.parity_decode_2chase(list(bpsk_par))
            dec1 = np.array(dec1[0, :], dtype=int)
            dec2 = np.array(dec2[0, :], dtype=int)

            # save outputs
            dec_err[i_mc, j, 0] = correct(dec1)
            dec_err[i_mc, j, 1] = correct(dec2)

        print(f"sigma={s} complete")

    linespecs = ['k^--', 'ko--']
    labels = ['JSCC: BCH-HD',  'JSCC: BCH-SD']
    for i in range(2):
        plt.semilogy(10*np.log10(SNRs), (1 - np.sum(dec_err, (0))[:, i]/n_mc), linespecs[i], label=labels[i])

    linespecs = ['r^-', 'ro-', 'r*-', 'r.-']
    labels = [f'SC: RS-HD CC: REP({i+1})' for i in range(rs_n_repeat)]
    for i in range(rs_n_repeat):
        plt.semilogy(10*np.log10(SNRs), (1 - np.sum(dec_err, (0))[:, 2 + i]/n_mc), linespecs[i], label=labels[i])


    plt.grid(which='major')
    plt.minorticks_on()
    plt.grid(which='minor')
    plt.xlabel("SNR (dB)")
    plt.ylabel("P(Error)")
    plt.legend()
    plt.title("Recovering |k|=3, t=5 Under Noise")
    plt.axis([-4, 8, 1e-3, 1])
    plt.show()




