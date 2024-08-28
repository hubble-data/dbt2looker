import logging
from typing import Optional
from functools import reduce

from ..parser import (
    parse_models,
    check_models_for_missing_column_types,
)


def parse_typed_models(
        raw_manifest: dict,
        tag: Optional[str] = None,
):
    dbt_models = parse_models(raw_manifest, tag=tag)
    logging.debug("Parsed %d models from manifest.json", len(dbt_models))
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        for model in dbt_models:
            logging.debug(
                "Model %s has %d columns with %d measures",
                model.name,
                len(model.columns),
                reduce(
                    lambda acc, col: acc
                                     + len(col.meta.measures)
                                     + len(col.meta.measure)
                                     + len(col.meta.metrics)
                                     + len(col.meta.metric),
                    model.columns.values(),
                    0,
                ),
            )

    logging.debug("Found manifest entries for %d models", len(dbt_models))
    check_models_for_missing_column_types(dbt_models)
    return dbt_models
