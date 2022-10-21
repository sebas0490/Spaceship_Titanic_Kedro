"""
This is a boilerplate pipeline 'featureEngineering'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.featureEngineering.nodes import (seleccionColumnsimpImpu,simplerImputer,renombrarColumnsTrain,renombrarColumnsTest,cambiarTipoDatoTransported,eliminarDuplicadosTrain,seleccionColumnas,overSample,ordinalE)
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=seleccionColumnsimpImpu,
            inputs=['datosSinDuplicados','data_limTest'],
            outputs=['X_train_num','x_train_cat','X_test_num','x_test_cat']
        ),

        node(
            func=simplerImputer,
            inputs=['X_train_num','x_train_cat','X_test_num','x_test_cat'],
            outputs=['X_transform_num','X_transform_cat','X_transform_num_test','X_transform_cat_test']
        ),
        node(
            func=renombrarColumnsTrain,
            inputs=['X_transform_num','X_transform_cat','X_train_num','x_train_cat'],
            outputs='X_traint_concat'
        ),
        node(
            func=renombrarColumnsTest,
            inputs=['X_transform_num_test','X_transform_cat_test','X_test_num','x_test_cat'],
            outputs='X_traint_concat_test'
        ),

        node(
            func=cambiarTipoDatoTransported,
            inputs='X_traint_concat',
            outputs='X_traint_df'
        ),
        node(
            func=eliminarDuplicadosTrain,
            inputs='X_traint_df',
            outputs='datosSinDuplicadosTrain'
        ),
        node(
            func=seleccionColumnas,
            inputs=['datosSinDuplicadosTrain','X_traint_concat_test'],
            outputs=['X_train', 'y_train','x_test','y_PassengerId']
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
