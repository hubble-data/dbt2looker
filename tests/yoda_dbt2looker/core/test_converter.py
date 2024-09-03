from tests.yoda_dbt2looker.test_cli import (
    assert_folders_equal,
    remove_folder_contents
)
from yoda_dbt2looker.core.converter import convert


class TestConverter:

    def test_run_convert(self):
        remove_folder_contents("generated_lookml")
        convert(
            target_dir="tests/resources/core/test_target",
            project_dir="tests/resources",
            output_dir="generated_lookml",
            tag="yoda_looker",
            log_level="INFO",
        )
        assert_folders_equal("tests/resources/core/expected_lookml/views", "generated_lookml")
