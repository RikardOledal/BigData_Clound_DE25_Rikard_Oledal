from pyspark import pipelines as dp
from pyspark.sql.types import StructType, StructField

BASE_DIR = "/Volumes/suppy_chain/default/raw"

# Infer schema from CSV
inferred_schema = spark.read.format("csv").options(header=True, inferSchema=True).load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv").schema

# Clean column names to remove invalid characters
def clean_column_name(name):
    return name.replace(" ", "_").replace("(", "").replace(")", "").replace(",", "")

schema = StructType([StructField(clean_column_name(field.name), field.dataType, field.nullable) for field in inferred_schema.fields])


@dp.table(name="suppy_chain.bronze.raw_supply_chain", comment="raw supply chain data for company X")
def raw_supply_chain():
  # Read with cleaned schema and rename columns to match
  df = spark.readStream.format("csv").options(header="true", encoding="UTF-8").schema(schema).load(f"{BASE_DIR}/data")
  return df