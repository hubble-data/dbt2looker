import logging
from typing import List, Dict, Any, Optional

from .utils import (
    get_manifest,
    get_dbt_project_config
)
from .config import config
from ..models import (
    DbtModel,
    DbtProjectConfig,
)
from ..parser import parse_dbt_project_config, parse_adapter_type
from yoda_dbt2looker.core.parser import parse_typed_models


def convert(target_dir=config.TARGET_DIR, project_dir=config.PROJECT_DIR, output_dir=config.LOOKML_OUTPUT_DIR, tag=None):
    """
    Convert dbt models to LookML views and models.

    This function performs the following steps:
    1. Retrieves the dbt manifest and project configuration
    2. Parses the dbt project config and models
    3. Determines the adapter type from the manifest
    4. Generates LookML views from the parsed dbt models
    5. Generates LookML models from the parsed dbt models

    Args:
        target_dir (str): Directory containing the dbt target files (default: config.TARGET_DIR)
        project_dir (str): Directory containing the dbt project files (default: config.PROJECT_DIR)
        output_dir (str): Directory to output the generated LookML files (default: config.LOOKML_OUTPUT_DIR)
        tag (str, optional): Tag to filter dbt models (default: None)

    Returns:
        None

    Raises:
        SystemExit: If there's an error in loading or parsing the dbt files
    """
    raw_manifest = get_manifest(prefix=target_dir)
    raw_config = get_dbt_project_config(prefix=project_dir)

    dbt_project_config = parse_dbt_project_config(raw_config)
    typed_dbt_models = parse_typed_models(raw_manifest, dbt_project_config.name, tag=tag)
    adapter_type = parse_adapter_type(raw_manifest)

    _generate_lookml_views(typed_dbt_models, adapter_type, output_dir)
    _generate_lookml_models(raw_manifest, typed_dbt_models, dbt_project_config, tag, output_dir)
    logging.info('Convertion finished successfully')


def _generate_lookml_views(typed_dbt_models: List[DbtModel], adapter_type: str, output_dir: str) -> None:
    pass


def _generate_lookml_models(raw_manifest: Dict[str, Any], typed_dbt_models: List[DbtModel],
                            dbt_project_config: DbtProjectConfig, tag: Optional[str], output_dir: str) -> None:
    pass
