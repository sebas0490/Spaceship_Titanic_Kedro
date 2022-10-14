"""
This is a boilerplate pipeline 'LimpiarDatos'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.LimpiarDatos.nodes import (eliminarColumnas,eliminarNulos,eliminarduplicados)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=eliminarColumnas,
            inputs=['df_train','df_test'],
            outputs=['data_limpia','data_limTest']
        ),


        node(
            func=eliminarduplicados,
            inputs='data_limpia',
            outputs='datos_sinDuplicados'
        ),
        node(
            func=eliminarNulos,
            inputs=['datos_sinDuplicados','data_limTest'],
            outputs=['datos_limpios','datosLimpiosTest']
        )


    ])
