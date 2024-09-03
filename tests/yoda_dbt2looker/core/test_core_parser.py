import pytest
from unittest.mock import patch
from yoda_dbt2looker.core import parser
from yoda_dbt2looker.core.models import DbtModel

# Mock data for testing

MOCK_MANIFEST = \
    {"metadata": {"adapter_type": "spark"},
     "nodes": {
         "model.playground.example_domain_stg__daily_model_a": {
             "name": "example_domain_stg__daily_model_a",
             "resource_type": "model",
             "schema": "dev",
             "relation_name": "dev_example_domain_stg__daily_model_a",
             "tags": [],
             "config": {
                 "tags": ["tag1"]
             },
             "unique_id": "model.playground.example_domain_stg__daily_model_a",
             "description": "Loyalty Stores Profile",
             "columns": {
                 "app_key": {
                     "name": "app_key",
                     "description": "TODO: Update Column app_key Information",
                     "meta": {},
                     "data_type": "string",
                 },
                 "a_time": {
                     "name": "a_time",
                     "description": "TODO: Update Column a_time Information",
                     "meta": {},
                     "data_type": "string",
                 },
                 "points_sum": {
                     "name": "points_sum",
                     "description": "TODO: Update Column points_sum Information",
                     "meta": {
                         "yoda_metric": {
                             "type": "sum"
                         }
                     },
                     "data_type": "bigint",
                 },
                 "time_id": {
                     "name": "time_id",
                     "description": "TODO: Update Column time_id Information",
                     "meta": {},
                     "data_type": "string",
                 }
             },
             "meta": {}

         },
         "model.playground.example_domain_stg__daily_model_b": {
             "name": "example_domain_stg__daily_model_b",
             "schema": "dev",
             "relation_name": "dev_example_domain_stg__daily_model_b",
             "resource_type": "model",
             "unique_id": "model.playground.example_domain_stg__daily_model_b",
             "tags": [],
             "config" : {
                 "tags": ["tag2"]
             },
             "description": "A starter dbt model",
             "columns": {
                 "id_key": {
                     "name": "id_key",
                     "description": "TODO: Update Column id_key Information",
                     "meta": {},
                     "data_type": "string",
                 },
                 "ref_time": {
                     "name": "ref_time",
                     "description": "TODO: Update Column ref_time Information",
                     "meta": {},
                     "data_type": "string",
                 },
             },
             "meta": {},
         },
     }
     }


@pytest.fixture
def raw_manifest():
    return MOCK_MANIFEST


class TestParser:
    @patch('yoda_dbt2looker.core.parser.parse_models')
    def test_parse_typed_models_without_tag(self, mock_parse_models, raw_manifest):
        mock_parse_models.return_value = [
            DbtModel(**MOCK_MANIFEST["nodes"]["model.playground.example_domain_stg__daily_model_a"]),
        ]
        result = parser.parse_typed_models(raw_manifest)
        assert len(result) == 1
        mock_parse_models.assert_called_once_with(raw_manifest, tag=None)

    @patch('yoda_dbt2looker.core.parser.parse_models')
    def test_parse_typed_models_with_tag(self, mock_parse_models, raw_manifest):
        mock_parse_models.return_value = [
            DbtModel(**MOCK_MANIFEST["nodes"]["model.playground.example_domain_stg__daily_model_b"]),
        ]
        result = parser.parse_typed_models(raw_manifest, tag="tag2")
        assert len(result) == 1
        assert result[0].name == "example_domain_stg__daily_model_b"
        mock_parse_models.assert_called_once_with(raw_manifest, tag="tag2")

    def test_parse_models_without_tag(self, raw_manifest):
        result = parser.parse_models(raw_manifest)
        assert len(result) == 2
        assert result[0].name == "example_domain_stg__daily_model_a"
        assert result[1].name == "example_domain_stg__daily_model_b"

    @patch('yoda_dbt2looker.parser.tags_match')
    def test_parse_models_with_tag(self, mock_tags_match, raw_manifest):
        mock_tags_match.return_value = True
        result = parser.parse_models(raw_manifest, tag="tag1")
        assert len(result) == 1
        assert result[0].name == "example_domain_stg__daily_model_a"

        mock_tags_match.return_value = False
        result = parser.parse_models(raw_manifest, tag="blabla")
        assert len(result) == 0

    def test_parse_models_raises_error_for_empty_model_file(self, raw_manifest):
        raw_manifest["nodes"]["model.playground.example_domain_stg__daily_model_a"].pop("name")
        with pytest.raises(SystemExit):
            parser.parse_models(raw_manifest)
