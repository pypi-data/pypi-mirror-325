import unittest
import numpy as np
import galois
from sparse_transform.qsft.utils.query import get_bch_decoder
from sparse_transform.qsft.codes.BCH import BCH

class TestCodes(unittest.TestCase):
    def setUp(self):
        # Initialize common test parameters
        self.n = 100
        self.t = 5
        self.bch = BCH(self.n, self.t)
        
        # Create test vector
        self.vec = np.zeros(self.n, dtype=int)
        self.vec[0] = 1
        self.vec[1] = 1
        self.vec[2] = 1
        self.vec = galois.GF2(self.vec)

    def test_bch_decoder_initialization(self):
        """Test if BCH decoder initializes for different parameters"""
        test_params = [
            (108, 11),
            (108, 12),
            (108, 13),
            (21, 5),
            (21, 6),
            (21, 7),
            (60, 12)
        ]
        
        for n, t in test_params:
            with self.subTest(n=n, t=t):
                decoder = get_bch_decoder(n, t)
                self.assertIsNotNone(decoder)

    def test_delay_matrices(self):
        """Test delay matrices generation"""
        P = self.bch.get_delay_matrix()
        self.assertIsNotNone(P)

    def test_decoding(self):
        """Test decoding"""
        P = self.bch.get_delay_matrix()
        par = np.array(P[1:] @ self.vec)
        dec, n = self.bch.parity_decode(list(par))
        dec = np.array(dec[0, :], dtype=int)
        self.assertTrue(all(x == y for x, y in zip(dec, self.vec)))

    def test_soft_decoding(self):
        """Test soft decoding with noise"""
        P = self.bch.get_delay_matrix()
        par = np.array(P[1:] @ self.vec)
        
        sigma = 0.7
        bpsk = (float(-1) ** par) + np.random.randn(len(par))*sigma/np.sqrt(2)
        dec3, n_err = self.bch.parity_decode_2chase(list(bpsk))
        dec3 = np.array(dec3[0, :], dtype=int)
        
        self.assertIsNotNone(dec3)
        self.assertTrue(isinstance(n_err, (int, float)))

if __name__ == '__main__':
    unittest.main()