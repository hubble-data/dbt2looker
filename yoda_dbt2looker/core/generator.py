import logging
from typing import List
from yoda_dbt2looker.core.models import DbtModel
import lkml

from yoda_dbt2looker.models import (
    SupportedDbtAdapters,
    LookViewFile
)
from yoda_dbt2looker.generator import (
    lookml_date_time_dimension_group,
    map_adapter_type_to_looker,
    lookml_date_dimension_group,
    looker_date_time_types,
    looker_date_types,
    looker_scalar_types,
    _generate_compound_primary_key_if_needed
)
from yoda_dbt2looker.core.utils import write_list_of_lookml_views
from yoda_dbt2looker.core.config import config


def generate_lookml_views(dbt_models: List[DbtModel], adapter_type: str, output_dir: str) -> None:
    views = [lookml_view_from_dbt_model(model, SupportedDbtAdapters(adapter_type)) for model in dbt_models]
    write_list_of_lookml_views(views, output_dir)


def lookml_view_from_dbt_model(model: DbtModel, adapter_type: SupportedDbtAdapters) -> LookViewFile:
    lookml = {
        "view": {
            "name": model.name,
            "sql_table_name": get_model_relation_name(model),
            "dimension_groups": lookml_dimension_groups_from_model(model, adapter_type),
            "dimensions": lookml_dimensions_from_model(model, adapter_type),
            # no measures will be created based on dbt models.
            "measures": [],
        }
    }
    logging.debug(
        f"Created view from model %s with %d dimensions",
        model.name,
        len(lookml["view"]["dimensions"]),
    )
    try:
        contents = lkml.dump(lookml)
    except Exception as e:
        logging.error(f"Error dumping lookml for model {model.name}")
        raise e
    return LookViewFile(filename=f"{model.name}.view.lkml", contents=contents)


def get_model_relation_name(model: DbtModel):
    if config.YODA_SNOWFLAKE_TAG in model.tags:
        return f"{model.meta.integration_config.snowflake.properties.sf_schema}.{model.meta.integration_config.snowflake.properties.table}"
    return model.relation_name


def lookml_dimension_groups_from_model(
        model: DbtModel, adapter_type: SupportedDbtAdapters
):
    date_times = [
        lookml_date_time_dimension_group(column, adapter_type)
        for column in model.columns.values()
        if map_adapter_type_to_looker(adapter_type, column.data_type)
           in looker_date_time_types
    ]
    dates = [
        lookml_date_dimension_group(column, adapter_type)
        for column in model.columns.values()
        if column.meta.dimension.enabled
           and map_adapter_type_to_looker(adapter_type, column.data_type)
           in looker_date_types
    ]

    return date_times + dates


def lookml_dimensions_from_model(model: DbtModel, adapter_type: SupportedDbtAdapters):
    dimensions = [
        {
            'name': column.meta.dimension.name or column.name,
            'type': map_adapter_type_to_looker(adapter_type, column.data_type),
            'sql': column.meta.dimension.sql or f'${{TABLE}}.{column.name}',
            'description': column.meta.dimension.description or column.description,
            **({"primary_key": "yes"} if model.meta.primary_key == column.name else {}),
            **(
                {'value_format_name': column.meta.dimension.value_format_name.value}
                if (column.meta.dimension.value_format_name
                    and map_adapter_type_to_looker(adapter_type, column.data_type) == 'number')
                else {}
            )
        }
        for column in model.columns.values()
        if column.meta.dimension.enabled
           and map_adapter_type_to_looker(adapter_type, column.data_type)
           in looker_scalar_types
    ]
    compound_key = _generate_compound_primary_key_if_needed(model)
    if compound_key:
        dimensions.append(compound_key)

    return dimensions
