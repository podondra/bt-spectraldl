import numpy as np
import imblearn.over_sampling
import sklearn.preprocessing


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
