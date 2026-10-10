# Real-Time Retail Intelligence Lakehouse

A portfolio project demonstrating retail data engineering using PySpark, Databricks, Delta Lake, and Structured Streaming.

## Project Overview

Retail businesses need reliable data pipelines to transform raw order data into accurate sales insights. This project demonstrates a lakehouse architecture that ingests retail data, validates and transforms records, produces analytical tables, and monitors data quality.

The project is developed using Databricks Free Edition with synthetic retail data.

## Architecture

```text
Retail CSV Files
      |
      v
Landing Volume
      |
      v
Bronze Layer
Raw order ingestion
      |
      v
Silver Layer
Validation, cleaning,
deduplication and merging
      |
      v
Gold Layer
Daily, product and
regional sales analytics
      |
      v
Business Reporting
Power BI / SQL Analytics

Supporting Components:
Data Quality | Checkpointing | Audit Logs
Automated Tests | Pipeline Validation
```

## Technology Stack

- **Python** — pipeline logic
- **PySpark** — distributed data processing
- **Databricks** — development and execution environment
- **Delta Lake** — transactional table storage and merge operations
- **Structured Streaming** — file-based incremental ingestion
- **SQL** — analytical queries and validation
- **Git and GitHub** — version control and documentation

## Project Modules

| Module | Description |
|---|---|
| Bronze ingestion | Load raw retail records |
| Silver transformation | Clean and validate records |
| Gold analytics | Generate daily, product and regional metrics |
| Incremental processing | Merge new records without duplicate inserts |
| File ingestion | Read CSV data from a landing volume |
| Structured Streaming | Process arriving files with checkpoints |
| Data quality monitoring | Check data completeness and validity |
| Pipeline orchestration | Coordinate processing and log run summaries |
| Automated testing | Test uniqueness, valid values and revenue reconciliation |
| Final validation | Consolidate project readiness checks |

## Data Quality Rules

The pipeline includes checks for:

- Missing order IDs
- Duplicate order IDs
- Invalid or missing order dates
- Missing product IDs
- Non-positive quantities
- Negative or missing unit prices
- Revenue reconciliation between Silver and Gold

## Repository Structure

```text
retail-intelligence-lakehouse/
├── README.md
├── .gitignore
├── notebooks/
│   ├── 01_retail_bronze_ingestion.py
│   ├── 02_retail_silver_transformation.py
│   ├── 03_retail_gold_analytics.py
│   ├── 04_retail_incremental_pipeline.py
│   ├── 05_retail_data_quality_monitoring.py
│   ├── 06_retail_pipeline_orchestrator.py
│   ├── 07_retail_file_ingestion.py
│   ├── 08_retail_incremental_file_ingestion.py
│   ├── 09_retail_structured_streaming.py
│   ├── 10_retail_incremental_silver.py
│   ├── 11_retail_pipeline_monitoring.py
│   ├── 12_retail_pipeline_orchestration.py
│   ├── 13_retail_business_analytics.py
│   ├── 14_retail_automated_testing.py
│   └── 15_retail_final_validation.py
├── src/
├── tests/
├── sql/
└── docs/
```

## How to Run

1. Create or open a Databricks Free Edition workspace.
2. Connect the GitHub repository to a Databricks Git folder.
3. Confirm the active catalog and create the required schema and landing volume.
4. Run the relevant ingestion notebook.
5. Run the transformation and analytics notebooks in dependency order.
6. Run the monitoring, testing and final validation notebooks.
7. Review the generated Delta tables and validation reports.

Check the setup requirements in the notebooks before executing them. Some notebooks use separate tables for the streaming demonstration.

## Limitations and Future Improvements

- The project currently uses synthetic data.
- File-based Structured Streaming is demonstrated; this is not a Kafka-based event streaming implementation.
- Some pipelines use full refreshes rather than fully incremental processing.
- Notebook-level orchestration is demonstrated; independent scheduled job tasks require additional configuration.
- Production deployment would require stronger access controls, alerting, recovery procedures, and broader integration testing.

## Project Status

Learning and portfolio project. Execution results and production-readiness claims will be documented after end-to-end testing.

## Author

**Vivek More**

Data Science | PySpark | Databricks | Data Engineering
