import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal

from context import braingraphgeo as bgg


def test_load_csv():
    path = 'somefile.txt'
    with pytest.raises(ValueError) as e_info:
        bgg.utils.load_connectivity_matrix(path)
    assert str(e_info.value) == 'Please enter the path to a .csv file'


def test_load_matrix_columns_match_index(sample_W_csv):
    W = bgg.utils.load_connectivity_matrix(sample_W_csv)
    columns = W.columns.values
    index = W.index.values
    assert_array_equal(columns, index)


def test_return_one_hemi(sample_W_csv):
    W = bgg.utils.load_connectivity_matrix(
        sample_W_csv, return_both_hemispheres=False)
    n1, n2 = W.shape
    assert n1 / n2 == 0.5


def test_build_spearman_matrix(sample_W_1, sample_W_2, parcellation):
    W1 = sample_W_1.values[:4]
    W2 = sample_W_2.values[:4]

    results = np.array([[1.,  0.2,  0.777778,  0.4],
                        [0.2,  1.,  0.4, -0.777778]])
    corr = bgg.utils.build_spearman_correlation_matrix(W1, W2, parcellation)
    assert_array_almost_equal(results, corr)


def test_spearman_wrong_shape(sample_W_1, sample_W_2, parcellation):
    W1 = sample_W_1.values[:4]
    W2 = sample_W_2.values[:5]

    with pytest.raises(ValueError) as e_info:
        corr = bgg.utils.build_spearman_correlation_matrix(
            W1, W2, parcellation)
    assert str(e_info.value) == 'mat1 and mat2 do not have the same shape'


def test_check_bad_parcellation(parcellation):
    parcellation.at[0, 'Brain Division'] = 'wrongname'
    with pytest.raises(ValueError) as e_info:
        bgg.utils.check_parcellation(parcellation)
    assert str(
        e_info.value) == 'Parcellation contains unknown acronym: wrongname'


def test_to_density(sample_W_1):
    W = sample_W_1.values
    W_thr = bgg.utils.to_density(W, 50)
    result = np.array([[0., 0.00069776, 0., 0.00044819, 0.00099724,
                        0.00054528, 0., 0.00074258],
                       [0.00069776, 0., 0.00053037, 0., 0.00054528,
                        0.00061656, 0., 0.],
                       [0., 0.00053037, 0., 0., 0.,
                        0., 0.00056931, 0.],
                       [0.00044819, 0., 0., 0., 0.00074258,
                        0., 0., 0.00064348],
                       [0.00099724, 0.00054528, 0., 0.00074258, 0.,
                        0.00069776, 0., 0.00044819],
                       [0.00054528, 0.00061656, 0., 0., 0.00069776,
                        0., 0.00053037, 0.],
                       [0., 0., 0.00056931, 0., 0.,
                        0.00053037, 0., 0.],
                       [0.00074258, 0., 0., 0.00064348, 0.00044819,
                        0., 0., 0.]])
    assert_array_almost_equal(W_thr, result)


def test_rescale():
    a = np.array([1, 2, 3])
    a_sc = bgg.utils.rescale(a)
    ans = [0., 0.5, 1.]
    assert_array_equal(a_sc, ans)
