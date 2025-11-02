from ligotools import utils
import numpy as np

def test_whiten_equal_length():
    fs = 4096
    dt = 1.0 / fs
    t = np.linspace(0, 1, fs)
    strain = np.sin(2 * np.pi * 60 * t)
    interp_psd = lambda f: np.ones_like(f)
    whitened = utils.whiten(strain, interp_psd, dt)
    assert len(whitened) == len(strain)

def test_reqshift_equal_length():
    data = np.sin(2 * np.pi * 60 * np.linspace(0, 1, 4096))
    shifted = utils.reqshift(data, fshift=100, sample_rate=4096)
    assert len(shifted) == len(data)