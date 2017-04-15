import urllib.request
import numpy as np


def retrieve_url(url):
    with urllib.request.urlopen(url) as f:
        data = f.read()
    return data

def cut_spectrum(waves, fluxes, start, end):
    '''Cut spectrum between start and end range.'''
    index = np.logical_and(start < waves, waves < end)
    return waves[index], fluxes[index]

def air2vacuum(air_waves):
    # http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion
    vac_waves = np.zeros_like(air_waves)
    for idx, wave in enumerate(air_waves):
        s = (10 ** 4) / wave
        n = 1 + 0.00008336624212083 + 0.02408926869968 / (130.1065924522 \
                - s ** 2) + 0.0001599740894897 / (38.92568793293 - s ** 2)
        vac_waves[idx] = wave * n
    return vac_waves
