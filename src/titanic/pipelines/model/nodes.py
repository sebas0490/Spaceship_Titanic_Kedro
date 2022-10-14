"""
This is a boilerplate pipeline 'model'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Tuple
from sklearn.model_selection import  GridSearchCV,train_test_split
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import (accuracy_score, f1_score, precision_score,make_scorer,
                             r2_score, recall_score, confusion_matrix)


def divirDataTrain(X_transformed:pd.DataFrame,y_overS:pd.DataFrame):
    X_Ttrain, X_Ttest, y_Otrain, y_Otest = train_test_split(X_transformed,y_overS, test_size=0.3, random_state=1)
    return X_Ttrain, X_Ttest, y_Otrain, y_Otest


def trainModeloTrain(X_Ttrain:pd.DataFrame,y_Otrain:pd.DataFrame):
    decision_tree_modelTrain = DecisionTreeClassifier(max_depth= 8).fit(X_Ttrain, y_Otrain)
    return decision_tree_modelTrain

def prediccion(decision_tree_modelTrain: DecisionTreeClassifier,X_Ttest:pd.DataFrame):
    y_predTrain = decision_tree_modelTrain.predict(X_Ttest)
    return y_predTrain

def validacionModel(y_Otest : pd.DataFrame,y_predTrain: pd.DataFrame):
    f1_score1 = f1_score(y_Otest , y_predTrain, average='macro')
    return f1_score1

def trainModelo(X_transformed:pd.DataFrame,y_overS:pd.DataFrame):
    decision_tree_model = DecisionTreeClassifier(max_depth= 8).fit(X_transformed, y_overS)
    return decision_tree_model

def prediccionModel(X_test_transformed: pd.DataFrame,decision_tree_model: DecisionTreeClassifier):
    y_test_pred = decision_tree_model.predict(X_test_transformed)
    return y_test_pred







