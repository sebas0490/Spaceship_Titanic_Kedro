"""
This is a boilerplate pipeline 'featureEngineering'
generated using Kedro 0.18.3
"""
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import OrdinalEncoder
from typing import Tuple
from sklearn.impute import SimpleImputer
import numpy as np


def seleccionColumnsimpImpu(datosSinDuplicados: pd.DataFrame,data_limTest:pd.DataFrame) ->Tuple[pd.DataFrame, pd.DataFrame,pd.DataFrame, pd.DataFrame]:
    X_train_num = datosSinDuplicados.drop(datosSinDuplicados.columns[[0, 1, 2, 3, 5, 11]], axis=1)
    x_train_cat = datosSinDuplicados.drop(datosSinDuplicados.columns[[4, 6, 7, 8, 9, 10]], axis=1)
    X_test_num = data_limTest.drop(data_limTest.columns[[0, 1, 2, 3,4, 6]], axis=1)
    x_test_cat = data_limTest.drop(data_limTest.columns[[5, 7, 8, 9, 10]], axis=1)

    return X_train_num,x_train_cat,X_test_num,x_test_cat



def simplerImputer(X_train_num:pd.DataFrame,x_train_cat:pd.DataFrame,X_test_num:pd.DataFrame,x_test_cat:pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame,pd.DataFrame, pd.DataFrame]:
    imp_mean_num = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_mean_cat = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    X_transform_num = imp_mean_num.fit_transform(X_train_num)
    X_transform_cat = imp_mean_cat.fit_transform(x_train_cat)

    X_transform_num_test = imp_mean_num.fit_transform(X_test_num)
    X_transform_cat_test = imp_mean_cat.fit_transform(x_test_cat)

    return X_transform_num,X_transform_cat,X_transform_num_test,X_transform_cat_test

def renombrarColumnsTrain(X_transform_num:pd.DataFrame,X_transform_cat:pd.DataFrame,X_train_num:pd.DataFrame,x_train_cat:pd.DataFrame)-> pd.DataFrame:
    X_traintTransColumn_num = pd.DataFrame(X_transform_num, columns=X_train_num.columns)
    X_traintTransColumn_cat = pd.DataFrame(X_transform_cat, columns=x_train_cat.columns)
    X_traint_concat = pd.concat([X_traintTransColumn_num, X_traintTransColumn_cat], axis=1)

    return X_traint_concat


def renombrarColumnsTest(X_transform_num_test:pd.DataFrame,X_transform_cat_test:pd.DataFrame,X_test_num: pd.DataFrame,x_test_cat:pd.DataFrame)-> pd.DataFrame:
    X_traintTransColumn_num = pd.DataFrame(X_transform_num_test, columns=X_test_num.columns)
    X_traintTransColumn_cat = pd.DataFrame(X_transform_cat_test, columns=x_test_cat.columns)
    X_traint_concat_test = pd.concat([X_traintTransColumn_num, X_traintTransColumn_cat], axis=1)

    return X_traint_concat_test

def cambiarTipoDatoTransported(X_traint_concat:pd.DataFrame)->pd.DataFrame:
    X_traint_concat['Transported'] = X_traint_concat['Transported'].astype('bool')
    X_traint_df = X_traint_concat
    return X_traint_df
def eliminarDuplicadosTrain(X_traint_df:pd.DataFrame)->pd.DataFrame:
    datosSinDuplicadosTrain = X_traint_df.drop_duplicates()

    return datosSinDuplicadosTrain



def seleccionColumnas(datosSinDuplicadosTrain: pd.DataFrame,X_traint_concat_test :pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    X_train = datosSinDuplicadosTrain[
        ['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'ShoppingMall',
         'Spa', 'VRDeck']]
    y_train = datosSinDuplicadosTrain['Transported']

    x_test= X_traint_concat_test[['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'ShoppingMall','Spa', 'VRDeck']]
    y_PassengerId=X_traint_concat_test[['PassengerId']]
    return X_train, y_train,x_test,y_PassengerId


def overSample(X_train: pd.DataFrame, y_train: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    os = RandomOverSampler()
    X_overS, y_overS = os.fit_resample(X_train, y_train)
    return X_overS, y_overS

def ordinalE(X_overS: pd.DataFrame,x_test:pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    oe = OrdinalEncoder()
    X_transformed = oe.fit_transform(X_overS)
    X_test_transformed = oe.fit_transform(x_test)
    return X_transformed,X_test_transformed






