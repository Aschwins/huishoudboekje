"""
This module contains all logic to extract the relevant information from a transactions.csv file downloaded from a dutch banking site.
"""

import pandas as pd
import numpy as np

def load_dataframe(filepath):
    df = pd.read_csv(filepath, delimiter=';')
    return df
