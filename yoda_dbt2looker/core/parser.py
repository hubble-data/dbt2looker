import logging
from typing import Optional, List, Dict
from functools import reduce
from yoda_dbt2looker.core.models import (
    DbtModel,
    DbtManifest
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
    return dbt_models


def parse_models(raw_manifest: Dict, tag: str = None) -> List[DbtModel]:
    manifest = DbtManifest(**raw_manifest)
    all_models: List[DbtModel] = [
        node for node in manifest.nodes.values() if node.resource_type == "model"
    ]

    # Empty model files have many missing parameters
    for model in all_models:
        if not hasattr(model, "name"):
            logging.error(
                'Cannot parse model with id: "%s" - is the model file empty?',
                model.unique_id,
            )
            raise SystemExit("Failed")

    if tag is None:
        return all_models
    return [model for model in all_models if tags_match(tag, model)]


def tags_match(query_tag: str, model: DbtModel) -> bool:
    try:
        return query_tag in model.config.tags
    except Exception as e:
        logging.error(f"Given tag {query_tag} doesn't exist in model config tags , err: {e}")
        return False
