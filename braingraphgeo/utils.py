import os
import pandas as pd


def load_data(path):
    '''
    Utility function to load graph adjacency matrix.

    Parameters
    __________
    path : str
        Path to data file. Must be .csv

    Returns
    _______
    df : DataFrame
        Adjacency matrix with node labels as pandas DataFrame


    '''
    if os.path.splitext(path)[1] != '.csv':
        raise ValueError('Please enter the path to a .csv file')

    df = pd.read_csv(path, index_col=0)
    return df
