import os
import pytest
import numpy as np
import pandas as pd


@pytest.fixture(scope='package')
def parcellation():
    data = {
        'Allen ID': [184, 985, 507, 151],
        'Acronym': ['FRP', 'Mop', 'MOB', 'AOB'],
        'Full Name': ['Frontal pole, cerebral cortex',
                      'Primary motor area',
                      'Main olfactory bulb',
                      'Accessory olfactory bulb'],
        'Brain Division': ['Isocortex', 'Isocortex', 'OLF', 'OLF']
    }
    return pd.DataFrame(data)


@pytest.fixture(scope='package')
def sample_W_1():
    np.random.seed(2021)
    N = 4
    Ntot = 8
    hemi = np.random.random((N, Ntot)) / 1e3
    full = np.zeros((Ntot, Ntot))
    full[:N] = hemi
    full[N:, :N] = hemi[:, N:]
    full[N:, N:] = hemi[:, :N]
    full = (full + full.T) / 2
    np.fill_diagonal(full, 0)

    nodes = ['FRP', 'Mop', 'MOB', 'AOB']
    labels_ipsi = [node + '-I' for node in nodes]
    labels_contra = [node + '-C' for node in nodes]
    labels = labels_ipsi + labels_contra

    W = pd.DataFrame(full, columns=labels, index=labels)

    return W


@pytest.fixture(scope='package')
def sample_W_2():
    np.random.seed(2022)
    N = 4
    Ntot = 8
    hemi = np.random.random((N, Ntot)) / 1e3
    full = np.zeros((Ntot, Ntot))
    full[:N] = hemi
    full[N:, :N] = hemi[:, N:]
    full[N:, N:] = hemi[:, :N]
    full = (full + full.T) / 2
    np.fill_diagonal(full, 0)

    nodes = ['FRP', 'Mop', 'MOB', 'AOB']
    labels_ipsi = [node + '-I' for node in nodes]
    labels_contra = [node + '-C' for node in nodes]
    labels = labels_ipsi + labels_contra

    W = pd.DataFrame(full, columns=labels, index=labels)

    return W


@pytest.fixture(scope='package')
def sample_W_csv(sample_W_1, tmp_path_factory):
    fn = tmp_path_factory.mktemp('data') / 'data_1.csv'
    sample_W_1.to_csv(fn)
    return fn


@pytest.fixture(scope='package')
def sample_D():
    np.random.seed(2023)
    N = 4
    Ntot = 8
    hemi = np.random.random((N, Ntot)) * 30
    full = np.zeros((Ntot, Ntot))
    full[:N] = hemi
    full[N:, :N] = hemi[:, N:]
    full[N:, N:] = hemi[:, :N]
    full = (full + full.T) / 2
    np.fill_diagonal(full, 0.5)

    nodes = ['FRP', 'Mop', 'MOB', 'AOB']
    labels_ipsi = [node + '-I' for node in nodes]
    labels_contra = [node + '-C' for node in nodes]
    labels = labels_ipsi + labels_contra

    D = pd.DataFrame(full, columns=labels, index=labels)

    return D


@pytest.fixture(scope='package')
def root_dir():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return root
