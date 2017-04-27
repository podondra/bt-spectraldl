import urllib.request
import numpy as np


def retrieve_url(url):
    with urllib.request.urlopen(url) as f:
        data = f.read()
    return data

def cut_spectrum(waves, fluxes, start, end):
    '''Cut spectrum between start and end range.'''
    index = (start < waves) & (waves < end)
    return waves[index], fluxes[index]
