"""
This is a boilerplate pipeline 'featureEngineering'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.featureEngineering.nodes import (seleccionColumnas,overSample,ordinalE)
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=seleccionColumnas,
            inputs=['datos_limpios','datosLimpiosTest'],
            outputs=['X_train', 'y_train','x_test']
        ),

        node(
            func=overSample,
            inputs=['X_train', 'y_train'],
            outputs=['X_overS', 'y_overS']
        ),
        node(
            func=ordinalE,
            inputs=['X_overS','x_test'],
            outputs=['X_transformed','X_test_transformed']
        )

    ])
