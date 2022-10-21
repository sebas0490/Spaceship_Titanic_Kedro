"""
This is a boilerplate pipeline 'ObtenerDatos'
generated using Kedro 0.18.3
"""
from typing import Tuple
import pandas as pd
from pathlib import Path


class Paths:
    data_path = Path(r'data').resolve().absolute()
    data_raw = data_path.joinpath(r'01_raw')
    path_train = data_raw.joinpath(r'train.csv')
    path_test = data_raw.joinpath(r'test.csv')


def get_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_train = pd.read_csv(Paths.path_train,  decimal='.')
    df_test = pd.read_csv(Paths.path_test, decimal='.')

    return ( df_train,df_test)
