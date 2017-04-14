import numpy as np


def compute_waves(hdulist):
    '''Computes LAMOST wavelengths.'''
    header = hdulist[0].header
    data = hdulist[0].data

    start = header['CRVAL1']
    delta = header['CD1_1']
    pix = header['CRPIX1']
    length = header['NAXIS1']

    waves = [10 ** (start + (i - pix + 1) * delta) for i in range(length)]
    
    return np.array(waves)

def plot_spectrum(hdulist, axes):
    '''Plot normalized LAMOST spectrum.'''
    waves = compute_waves(hdulist)
    fluxes = hdulist[0].data[2]

    return axes.plot(waves, fluxes)

def get_waves(hdulist):
    return compute_waves(hdulist)

def get_fluxes(hdulist):
    return hdulist[0].data[2]
