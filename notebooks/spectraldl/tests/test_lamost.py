import astropy.io.fits
import spectraldl.lamost
import numpy as np


def test_compute_waves():
    with astropy.io.fits.open('data/bt-cmi-lamost.fits') as hdulist:
        waves = spectraldl.lamost.compute_waves(hdulist)
    assert isinstance(waves, np.ndarray)
    assert round(waves[0]) == 3700.0
    assert round(waves[-1]) == 9078.0
    assert len(waves) == 3899

def test_get_fluxes():
    with astropy.io.fits.open('data/bt-cmi-lamost.fits') as hdulist:
        fluxes = spectraldl.lamost.get_fluxes(hdulist)
    assert isinstance(fluxes, np.ndarray)
    assert len(fluxes) == 3899
