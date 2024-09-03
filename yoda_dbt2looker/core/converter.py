import logging
from .utils import (
    get_manifest,
    get_dbt_project_config,
    configure_logging
)
from .config import config
from ..parser import (
    parse_dbt_project_config,
    parse_adapter_type,
)
from yoda_dbt2looker.core.parser import parse_typed_models
from yoda_dbt2looker.core.generator import generate_lookml_views


def convert(target_dir=config.TARGET_DIR, project_dir=config.PROJECT_DIR, output_dir=config.LOOKML_OUTPUT_DIR,
            tag=None, log_level=config.LOG_LEVEL):
    """
    Convert dbt models to LookML views and models.

    This function automates the conversion of dbt models into LookML by performing the following steps:
    1. Retrieves the dbt manifest and project configuration from the specified directories.
    2. Parses the dbt project configuration and models to extract necessary details.
    3. Determines the appropriate adapter type from the manifest to tailor the LookML generation.
    4. Generates LookML views based on the parsed dbt models, ensuring compatibility and accuracy.
    5. Generates LookML models, which define how the views are combined and queried.

    :param target_dir: The directory containing the dbt target files (default: config.TARGET_DIR).
    :type target_dir: str
    :param project_dir: The directory containing the dbt project files (default: config.PROJECT_DIR).
    :type project_dir: str
    :param output_dir: The directory where the generated LookML files will be saved (default: config.LOOKML_OUTPUT_DIR).
    :type output_dir: str
    :param tag: A specific tag used to filter which dbt models to convert (default: None).
    :type tag: str, optional
    :param log_level: The level of logging detail (default: config.LOG_LEVEL).
    :type log_level: str

    :returns: None

    :raises SystemExit: If there is an error in loading, parsing, or processing the dbt files, the function will terminate the program.
    """
    configure_logging(log_level)
    raw_manifest = get_manifest(prefix=target_dir)
    typed_dbt_models = parse_typed_models(raw_manifest, tag=tag)
    adapter_type = parse_adapter_type(raw_manifest)

    generate_lookml_views(typed_dbt_models, adapter_type, output_dir)
    logging.info('Convertion finished successfully')
