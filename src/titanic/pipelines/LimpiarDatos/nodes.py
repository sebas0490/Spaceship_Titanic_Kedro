"""
This is a boilerplate pipeline 'LimpiarDatos'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Tuple








def eliminarColumnas(df_train: pd.DataFrame,df_test: pd.DataFrame) -> pd.DataFrame:
    data_limpia = df_train.drop(['Name', 'PassengerId'], axis=1)
    data_limTest = df_test.drop('Name', axis=1)

    return data_limpia,data_limTest




def eliminarduplicados(data_limpia: pd.DataFrame) -> pd.DataFrame:
    datosSinDuplicados = data_limpia.drop_duplicates()
    return datosSinDuplicados





