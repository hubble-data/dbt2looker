from dataclasses import dataclass


@dataclass
class Config:
    LOOKML_OUTPUT_DIR: str = './lookml'
    TARGET_DIR: str = './target'
    PROJECT_DIR: str = './'
    LOG_LEVEL: str = 'INFO'
    MANIFEST_FILENAME: str = 'manifest.json'
    DBT_PROJECT_FILENAME: str = 'dbt_project.yml'


config = Config()
