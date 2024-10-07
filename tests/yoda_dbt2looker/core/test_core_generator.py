from unittest.mock import patch, MagicMock, call
from yoda_dbt2looker.models import SupportedDbtAdapters, LookViewFile
from yoda_dbt2looker.core import generator
from yoda_dbt2looker.core.models import DbtModel, DbtModelMeta
from yoda_dbt2looker.core.config import config


class TestGenerator:

    @patch('yoda_dbt2looker.core.generator.write_list_of_lookml_views')
    @patch('yoda_dbt2looker.core.generator.lookml_view_from_dbt_model')
    def test_generate_lookml_views(self, mock_lookml_view_from_dbt_model, mock_write_list_of_lookml_views):
        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_lookml_view = MagicMock(spec=LookViewFile)
        mock_lookml_view_from_dbt_model.return_value = mock_lookml_view

        generator.generate_lookml_views([mock_dbt_model], "snowflake", "output/dir")

        mock_lookml_view_from_dbt_model.assert_called_once_with(mock_dbt_model, SupportedDbtAdapters.snowflake)
        mock_write_list_of_lookml_views.assert_called_once_with([mock_lookml_view], "output/dir")

    @patch('yoda_dbt2looker.core.generator.lkml.dump')
    def test_lookml_view_from_dbt_model(self, mock_lkml_dump):
        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_dbt_model.name = "test_model"
        mock_dbt_model.relation_name = "test_model"
        mock_dbt_model.columns = {}
        mock_dbt_model.tags = []
        mock_dbt_model.meta = MagicMock(spec=DbtModelMeta)
        mock_dbt_model.meta.primary_key = ""
        mock_lkml_dump.return_value = "lookml_content"

        result = generator.lookml_view_from_dbt_model(mock_dbt_model, SupportedDbtAdapters.snowflake)

        assert isinstance(result, LookViewFile)
        assert result.filename == "test_model.view.lkml"
        assert result.contents == "lookml_content"
        mock_lkml_dump.assert_called_once()

    def test_get_model_relation_name_with_tag(self):
        mock_snowflake_properties = MagicMock()
        mock_snowflake_properties.sf_schema = "test_schema"
        mock_snowflake_properties.table = "test_table"

        mock_snowflake_integration = MagicMock()
        mock_snowflake_integration.properties = mock_snowflake_properties

        mock_integration_config = MagicMock()
        mock_integration_config.snowflake = mock_snowflake_integration

        mock_meta = MagicMock(spec=DbtModelMeta)
        mock_meta.integration_config = mock_integration_config

        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_dbt_model.tags = [config.YODA_SNOWFLAKE_TAG]
        mock_dbt_model.meta = mock_meta

        result = generator.get_model_relation_name(mock_dbt_model)
        assert result == "test_schema.test_table"

    def test_get_model_relation_name_without_tag(self):
        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_dbt_model.tags = []
        mock_dbt_model.relation_name = "relation_name"

        result = generator.get_model_relation_name(mock_dbt_model)
        assert result == "relation_name"

    @patch('yoda_dbt2looker.core.generator.lookml_date_time_dimension_group')
    @patch('yoda_dbt2looker.core.generator.lookml_date_dimension_group')
    @patch('yoda_dbt2looker.core.generator.map_adapter_type_to_looker')
    def test_lookml_dimension_groups_from_model(self, mock_map_adapter_type_to_looker, mock_lookml_date_dimension_group,
                                                mock_lookml_date_time_dimension_group):
        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_column_1 = MagicMock()
        mock_column_1.meta.dimension.enabled = True
        mock_column_1.data_type = "timestamp"
        mock_column_2 = MagicMock()
        mock_column_2.meta.dimension.enabled = True
        mock_column_2.data_type = "date"
        mock_dbt_model.columns = {"col1": mock_column_1, "col2": mock_column_2}

        mock_map_adapter_type_to_looker.side_effect = [
            "timestamp",
            "timestamp",
            "datetime",
            "datetime",
            "timestamp",
            "timestamp",
            "datetime",
            "datetime",
        ]
        mock_lookml_date_time_dimension_group.return_value = "datetime_group"

        result = generator.lookml_dimension_groups_from_model(mock_dbt_model, SupportedDbtAdapters.spark.value)

        assert result == ["datetime_group", "datetime_group"]
        mock_lookml_date_time_dimension_group.assert_has_calls(
            [call(mock_column_1, SupportedDbtAdapters.spark), call(mock_column_2, SupportedDbtAdapters.spark)])

        result = generator.lookml_dimension_groups_from_model(
            mock_dbt_model, SupportedDbtAdapters.databricks.value
        )

        assert result == ["datetime_group", "datetime_group"]
        mock_lookml_date_time_dimension_group.assert_has_calls(
            [
                call(mock_column_1, SupportedDbtAdapters.databricks),
                call(mock_column_2, SupportedDbtAdapters.databricks),
            ]
        )

    @patch('yoda_dbt2looker.core.generator.map_adapter_type_to_looker')
    def test_lookml_dimensions_from_model(self, mock_map_adapter_type_to_looker):
        mock_dbt_model = MagicMock(spec=DbtModel)
        mock_column = MagicMock()
        mock_column.name = "test_column"
        mock_column.data_type = "integer"
        mock_column.description = "test column"
        mock_column.meta.dimension.enabled = True
        mock_column.meta.dimension.sql = None
        mock_column.meta.dimension.name = None
        mock_column.meta.dimension.description = None
        mock_column.meta.dimension.value_format_name = None
        mock_dbt_model.columns = {"col1": mock_column}
        mock_dbt_model.meta = MagicMock(spec=DbtModelMeta)
        mock_dbt_model.meta.primary_key = ""

        mock_map_adapter_type_to_looker.return_value = "number"

        result = generator.lookml_dimensions_from_model(mock_dbt_model, SupportedDbtAdapters.spark)

        expected_dimension = {
            'name': "test_column",
            'type': "number",
            'sql': "${TABLE}.test_column",
            'description': "test column"
        }
        assert result == [expected_dimension]
        mock_map_adapter_type_to_looker.assert_has_calls([call(SupportedDbtAdapters.spark, "integer")
                                                             , call(SupportedDbtAdapters.spark, "integer")])
        result = generator.lookml_dimensions_from_model(
            mock_dbt_model, SupportedDbtAdapters.databricks
        )

        expected_dimension = {
            "name": "test_column",
            "type": "number",
            "sql": "${TABLE}.test_column",
            "description": "test column",
        }
        assert result == [expected_dimension]
        mock_map_adapter_type_to_looker.assert_has_calls(
            [
                call(SupportedDbtAdapters.databricks, "integer"),
                call(SupportedDbtAdapters.databricks, "integer"),
            ]
        )
