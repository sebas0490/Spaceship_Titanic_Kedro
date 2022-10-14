"""
This is a boilerplate pipeline 'featureEngineering'
generated using Kedro 0.18.3
"""
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import OrdinalEncoder
from typing import Tuple


def seleccionColumnas(datos_limpios: pd.DataFrame,datosLimpiosTest :pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    X_train = datos_limpios[
        ['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'ShoppingMall',
         'Spa', 'VRDeck']]
    y_train = datos_limpios['Transported']

    x_test= datosLimpiosTest[['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'ShoppingMall','Spa', 'VRDeck']]
    return X_train, y_train,x_test


def overSample(X_train: pd.DataFrame, y_train: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    os = RandomOverSampler()
    X_overS, y_overS = os.fit_resample(X_train, y_train)
    return X_overS, y_overS

def ordinalE(X_overS: pd.DataFrame,x_test:pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    oe = OrdinalEncoder()
    X_transformed = oe.fit_transform(X_overS)
    X_test_transformed = oe.fit_transform(x_test)
    return X_transformed,X_test_transformed






