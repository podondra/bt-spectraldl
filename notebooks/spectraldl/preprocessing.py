import numpy as np
import imblearn.over_sampling
import sklearn.preprocessing
import astropy.convolution


START = 6519
END = 6732

def air2vacuum(air_waves):
    '''Convert air wavelengths to vacuum wavelengths'''
    # http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion
    vac_waves = np.zeros_like(air_waves)
    for idx, wave in enumerate(air_waves):
        s = (10 ** 4) / wave
        n = 1 + 0.00008336624212083 + 0.02408926869968 / (130.1065924522 \
                - s ** 2) + 0.0001599740894897 / (38.92568793293 - s ** 2)
        vac_waves[idx] = wave * n
    return vac_waves

def convolve_spectrum(fluxes, stddev=7):
    '''Convolve spectrum with Gaussian 1D kernel.'''
    kernel = astropy.convolution.Gaussian1DKernel(stddev=stddev)
    return astropy.convolution.convolve(fluxes, kernel, boundary='extend')

def resample_spectrum(waves, fluxes, space=np.linspace(START, END, 140)):
    return np.interp(space, waves, fluxes)

def smote_over_sample(X, y, *, n_classes):
    '''Oversample the dataset
    so that all classes has the same number of samples.'''
    X_ = np.copy(X)
    y_ = np.copy(y)

    smote = imblearn.over_sampling.SMOTE()
    for _ in range(n_classes - 1):
        X_, y_ = smote.fit_sample(X_, y_)

    return X_, y_

def scale_samples(X_train, X_validation):
    '''Scale each sample to have zero mean and unit sample.'''
    X_tr = sklearn.preprocessing.scale(X_train, axis=1)
    X_val = sklearn.preprocessing.scale(X_validation, axis=1)
    return X_tr, X_val

def scale_features(X_train, X_validation,
        scaler=sklearn.preprocessing.StandardScaler()):
    '''Fit scaler on X_train and tranform both X_train and X_validation.'''
    X_tr = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_validation)
    return X_tr, X_val
