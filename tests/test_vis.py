import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from context import braingraphgeo as bgg


@pytest.mark.filterwarnings('ignore::RuntimeWarning')
def download_connectivity_matrix(root_dir):
    tracer_fn = f'{root_dir}/data/tracer.csv'
    W = bgg.utils.load_connectivity_matrix(tracer_fn).values[:286]
    parcel = pd.read_csv(f'{root_dir}/data/parcellation.csv')
    with np.errstate(divide='ignore'):
        fig, ax = bgg.vis.connectivity_matrix(np.log10(W), parcel, -7.5, -2.5)
    fig.savefig(f'{root_dir}/tests/test_connectivity_matrix.png')


def download_spearman_matrix(root_dir):
    tracer_fn = f'{root_dir}/data/tracer.csv'
    tracer = bgg.utils.load_connectivity_matrix(tracer_fn).values[:286]
    tract_fn = f'{root_dir}/data/tract_dense_n1.csv'
    tract = bgg.utils.load_connectivity_matrix(tract_fn).values[:286]
    parcel = pd.read_csv(f'{root_dir}/data/parcellation.csv')

    corr = bgg.utils.build_spearman_correlation_matrix(tracer, tract, parcel)
    fig, ax = bgg.vis.plot_spearman_correlation_matrix(corr)
    fig.savefig(f'{root_dir}/tests/test_corr_matrix.png')


def download_dict():
    return {'connectivity_matrix': download_connectivity_matrix,
            'corr_matrix': download_spearman_matrix}


def assert_close(a, b):
    mismatch = np.sum(a != b)
    ratio = mismatch / a.size
    if ratio <= 0.01:
        assert True
    if ratio > 0.01:
        assert False


@pytest.mark.filterwarnings('ignore::DeprecationWarning')
@pytest.mark.parametrize('figure_str', ['connectivity_matrix', 'corr_matrix'])
def test_figures(root_dir, figure_str):
    download_func = download_dict()[figure_str]
    download_func(root_dir)
    test_img = plt.imread(
        f'{root_dir}/tests/test_{figure_str}.png')
    true_img = plt.imread(
        f'{root_dir}/tests/benchmarks/{figure_str}.png')
    assert_close(true_img, test_img)


def test_corr_wrong_shape():
    corr = np.zeros((12, 23))
    with pytest.raises(ValueError) as e_info:
        bgg.vis.plot_spearman_correlation_matrix(corr)
    assert str(e_info.value) == 'Incorrect brain divisions'
