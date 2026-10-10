
# Keep common Silver transformations in one place
from pyspark.sql import functions as F


def prepare_orders_for_silver(orders_df):
    # Convert the raw date string into a date
    prepared_df = orders_df.withColumn(
        "order_date",
        F.to_date("order_date", "yyyy-MM-dd")
    )

    # Keep one record per order ID for this example
    prepared_df = prepared_df.dropDuplicates(["order_id"])

    # Separate valid records from records needing review
    valid_condition = (
        F.col("order_id").isNotNull()
        & F.col("order_date").isNotNull()
        & F.col("product_id").isNotNull()
        & F.col("quantity").isNotNull()
        & (F.col("quantity") > 0)
        & F.col("unit_price").isNotNull()
        & (F.col("unit_price") >= 0)
    )

    valid_orders = prepared_df.filter(valid_condition)
    invalid_orders = prepared_df.filter(~valid_condition)

    return valid_orders, invalid_orders
