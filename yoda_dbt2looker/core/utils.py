import json
import logging
import os
import yaml
from typing import Dict, List, Any
from pathlib import Path

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from .. import parser
from ..models import LookViewFile
from .config import config


def configure_logging(log_level: str = config.LOG_LEVEL):
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s %(levelname)-6s %(message)s',
        datefmt='%H:%M:%S',
    )


def write_lookml_file(file_path: str, contents: str) -> None:
    with open(file_path, 'w') as f:
        f.write(contents)


def write_list_of_lookml_views(views: List[LookViewFile], output_dir: str = config.LOOKML_OUTPUT_DIR) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for view in views:
        file_path = os.path.join(output_dir, view.filename)
        write_lookml_file(file_path, view.contents)


def load_json_file(file_path: Path) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f'Could not find file at {file_path}.')
        raise SystemExit(f'Failed to load json file: {file_path}')


def load_yaml_file(file_path: Path) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return yaml.load(f, Loader=Loader)
    except FileNotFoundError:
        logging.error(f'Could not find file at {file_path}.')
        raise SystemExit(f'Failed to load yaml file: {file_path}')


def get_manifest(prefix: str) -> Dict[str, Any]:
    manifest_path = os.path.join(prefix, config.MANIFEST_FILENAME)
    raw_manifest = load_json_file(manifest_path)
    parser.validate_manifest(raw_manifest)
    logging.debug(f'Detected valid manifest at {manifest_path}')
    return raw_manifest


def get_dbt_project_config(prefix: str) -> Dict[str, Any]:
    project_path = os.path.join(prefix, config.DBT_PROJECT_FILENAME)
    project_config = load_yaml_file(project_path)
    logging.debug(f'Detected valid dbt config at {project_path}')
    return project_config
