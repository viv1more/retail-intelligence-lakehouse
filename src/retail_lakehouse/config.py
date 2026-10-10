
# Keep the project table names and paths in one place

def get_project_config(spark, schema_name="retail_lakehouse"):
    catalog = spark.sql(
        "SELECT current_catalog()"
    ).first()[0]

    base_path = f"/Volumes/{catalog}/{schema_name}/retail_landing"

    return {
        "catalog": catalog,
        "schema": schema_name,
        "volume_path": base_path,

        # Main batch pipeline
        "bronze_orders": f"{catalog}.{schema_name}.bronze_orders",
        "bronze_products": f"{catalog}.{schema_name}.bronze_products",
        "silver_orders": f"{catalog}.{schema_name}.silver_orders",
        "gold_daily_sales": f"{catalog}.{schema_name}.gold_daily_sales",
        "gold_product_performance":
            f"{catalog}.{schema_name}.gold_product_performance",
        "gold_regional_sales":
            f"{catalog}.{schema_name}.gold_regional_sales",

        # Streaming demonstration
        "streaming_bronze":
            f"{catalog}.{schema_name}.streaming_orders_bronze",
        "streaming_silver":
            f"{catalog}.{schema_name}.streaming_orders_silver",
        "streaming_gold_daily":
            f"{catalog}.{schema_name}.streaming_gold_daily_sales",
        "streaming_gold_product":
            f"{catalog}.{schema_name}.streaming_gold_product_performance",
        "streaming_gold_regional":
            f"{catalog}.{schema_name}.streaming_gold_regional_sales",

        # Monitoring and testing
        "quality_audit":
            f"{catalog}.{schema_name}.streaming_data_quality_audit",
        "test_history":
            f"{catalog}.{schema_name}.automated_test_history",
        "pipeline_run_log":
            f"{catalog}.{schema_name}.pipeline_run_log",
        "validation_report":
            f"{catalog}.{schema_name}.final_validation_report",
    }
