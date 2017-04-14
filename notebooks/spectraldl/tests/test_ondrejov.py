import astropy.io.fits
import spectraldl.ondrejov
import numpy as np


def test_get_waves():
    with astropy.io.fits.open('samples/bt-cmi-ondrejov.fits') as hdulist:
        waves = spectraldl.ondrejov.get_waves(hdulist)
    assert isinstance(waves, np.ndarray)
    assert len(waves) == 1953

def test_get_fluxes():
    with astropy.io.fits.open('samples/bt-cmi-ondrejov.fits') as hdulist:
        fluxes = spectraldl.ondrejov.get_fluxes(hdulist)
    assert isinstance(fluxes, np.ndarray)
    assert len(fluxes) == 1953
