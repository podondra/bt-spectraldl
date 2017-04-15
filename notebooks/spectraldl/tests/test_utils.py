import spectraldl.utils
import numpy as np


def test_retrieve_url():
    data = spectraldl.utils.retrieve_url('http://httpbin.org')
    assert data != ''

def test_cut_spectrum():
    x, y = np.arange(10), np.arange(10, 0, -1)
    x_new, y_new = spectraldl.utils.cut_spectrum(x, y, 2.5, 7.5)
    assert np.all(x_new == np.arange(3, 8))
    assert np.all(y_new == np.array([7, 6, 5, 4, 3]))

def test_air2vacuum():
    waves = spectraldl.utils.air2vacuum(np.array([10], dtype=np.float))
    assert abs(waves[0] - 10.00083342) < 0.00000001
