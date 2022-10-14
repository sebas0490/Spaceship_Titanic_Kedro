"""
This is a boilerplate pipeline 'model'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.model.nodes import (divirDataTrain,trainModeloTrain,prediccion,validacionModel,trainModelo,prediccionModel)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=divirDataTrain,
            inputs=['X_transformed','y_overS'],
            outputs=['X_Ttrain', 'X_Ttest', 'y_Otrain', 'y_Otest']
        ),
        node(
            func=trainModeloTrain,
            inputs=['X_Ttrain','y_Otrain'],
            outputs='decision_tree_modelTrain'
        ),
        node(
            func=prediccion,
            inputs=['decision_tree_modelTrain','X_Ttest'],
            outputs='y_predTrain'
        ),
        node(
            func=validacionModel,
            inputs=['y_Otest','y_predTrain'],
            outputs='f1_score1'
        ),
        node(
            func=trainModelo,
            inputs=['X_transformed','y_overS'],
            outputs='decision_tree_model'
        ),
        node(
            func=prediccionModel,
            inputs=['X_test_transformed', 'decision_tree_model'],
            outputs='y_test_pred'
        )


    ])
