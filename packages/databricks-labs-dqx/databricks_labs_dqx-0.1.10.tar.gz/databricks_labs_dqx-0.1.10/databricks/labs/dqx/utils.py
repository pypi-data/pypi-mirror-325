import re
import yaml
from pyspark.sql import Column
from pyspark.sql import SparkSession


STORAGE_PATH_PATTERN = re.compile(r"^(/|s3:/|abfss:/|gs:/)")
UNITY_CATALOG_TABLE_PATTERN = re.compile(r"^[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$")


def get_column_name(col: Column) -> str:
    """
    PySpark doesn't allow to directly access the column name with respect to aliases from an unbound column.
    It is necessary to parse this out from the string representation.

    This works on columns with one or more aliases as well as not aliased columns.

    :param col: Column
    :return: Col name alias as str
    """
    return str(col).removeprefix("Column<'").removesuffix("'>").split(" AS ")[-1]


def read_input_data(spark: SparkSession, input_location: str | None, input_format: str | None):
    """
    Reads input data from the specified location and format.

    :param spark: SparkSession
    :param input_location: The input data location.
    :param input_format: The input data format.
    """
    if not input_location:
        raise ValueError("Input location not configured")

    if UNITY_CATALOG_TABLE_PATTERN.match(input_location):
        return spark.read.table(input_location)  # must provide 3-level Unity Catalog namespace

    if STORAGE_PATH_PATTERN.match(input_location):
        if not input_format:
            raise ValueError("Input format not configured")
        return spark.read.format(str(input_format)).load(input_location)

    raise ValueError(
        f"Invalid input location. It must be Unity Catalog table / view or storage location, " f"given {input_location}"
    )


def deserialize_dicts(checks: list[dict[str, str]]) -> list[dict]:
    """
    deserialize string fields instances containing dictionaries
    @param checks: list of checks
    @return:
    """
    for item in checks:
        for key, value in item.items():
            if value.startswith("{") and value.endswith("}"):
                item[key] = yaml.safe_load(value.replace("'", '"'))
    return checks
