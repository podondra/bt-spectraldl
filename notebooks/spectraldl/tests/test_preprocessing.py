import spectraldl.preprocessing
import numpy as np


EPS = 10e-6

def test_smote_over_sample():
    X, y = np.random.rand(100, 1), np.random.randint(2, size=100)
    X_, y_ = spectraldl.preprocessing.smote_over_sample(X, y, n_classes=2)
    _, counts = np.unique(y_, return_counts=True) 
    assert counts[0] == counts[1]

def test_scale_samples():
    X, Y = np.random.rand(100, 50), np.random.rand(100, 50)
    X_, Y_ = spectraldl.preprocessing.scale_samples(X, Y)
    assert np.all(np.abs(X_.mean(axis=1)) < EPS)
    assert np.all((np.abs(X_.std(axis=1)) - 1) < EPS)

def test_scale_samples():
    X, Y = np.random.rand(100, 50), np.random.rand(100, 50)
    X_, Y_ = spectraldl.preprocessing.scale_features(X, Y)
    assert np.all(np.abs(X_.mean(axis=0)) < 10e-6)
    assert np.all((np.abs(X_.std(axis=0)) - 1) < EPS)
