"""
This is a boilerplate pipeline 'ObtenerDatos'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.ObtenerDatos.nodes import  get_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=get_data,
            inputs=None,
            outputs=['df_train','df_test']
        )


    ])
