from pyspark import pipelines as dp
from utils.utils import rename_columns_to_snake_case
from pyspark.sql.functions import to_timestamp, col, coalesce, lit, when, round


@dp.table(
    name="supply_chain.2_silver.supply_chain_obt",
    comment="Cleaned supply chain data for company DataCo",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5",
    },
)
def clean_supply_chain():
    df = spark.sql("FROM STREAM supply_chain.1_bronze.raw_supply_chain")
    df = rename_columns_to_snake_case(df)
    return (
        df.withColumn(
            "shipping_date", to_timestamp("shipping_date_dateorders", "M/d/yyyy H:mm")
        )
        .withColumn(
            "order_zipcode", coalesce(col("order_zipcode").cast("string"), lit("unknown"))
        )
        .withColumn(
            "customer_zipcode",
             coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        ).withColumn(
            "customer_country", when(col("customer_country") == "EE. UU.", "United States").otherwise(col("customer_country"))
        ).withColumn(
            "order_date", to_timestamp("order_date_dateorders", "M/d/yyyy H:mm")
        ).withColumn(
            "benefit_per_order_dec", round("benefit_per_order", 2)
        ).withColumn(
            "sales_per_customer_dec", round("sales_per_customer", 2)
        ).withColumn(
            "order_item_product_price_dec", round("order_item_product_price", 2)
        ).drop(
            "customer_email",
            "customer_password",
            "product_description",
            "shipping_date_dateorders",
            "order_date_dateorders",
            "benefit_per_order",
            "sales_per_customer",
            "order_item_product_price"
        )
    )




