[![CI](https://github.com/nogibjj/Mobasserul_Haque_MiniProject5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mobasserul_Haque_MiniProject5/actions/workflows/cicd.yml)

# Graduate Employment Salary ETL Query Pipeline using Databricks

This project provides an ETL (Extract, Transform, Load) and querying tool designed to analyze critical employment statistics for both undergraduate and graduate students. The analysis focuses on employment rates, unemployment rates, and salary premiums, leveraging data from the **RecentGradsDB** and **GradStudentsDB** datasets.

The pipeline is built using Python and Databricks, offering users the capability to efficiently extract data from various sources, transform and clean it for analysis, and load it into a Databricks table for further processing. Users can perform complex SQL queries that utilize JOINs, aggregations, filtering, and sorting to gain insights into employment trends, average salaries, and the effectiveness of various degree programs in securing employment for graduates.

By utilizing this pipeline, educators, policymakers, and students can better understand the labor market dynamics and the value of different degrees, ultimately aiding in informed decision-making regarding education and career paths.

## Features

- **ETL Operations**: 
  - Extract data from CSV files.
  - Transform and load data into Databricks tables for analysis.
  
- **Data Transformation**: Cleaning and preprocessing of data to ensure consistency and accuracy, including handling missing values and converting data types.

- **Data Loading**: Efficient loading of transformed data into a Databricks table, enabling scalable querying and analysis.

- **Query Operations**:
  - Execute complex SQL queries using JOINs, GROUP BY, HAVING, and UNION.
  - Filter and sort data by employment rates, salary differences, and other attributes.
  
- **Logging and Output**:
  - Query results are outputted in a structured format for easy interpretation.
  - Errors and exceptions are logged during ETL and querying processes.

## Directory Structure

```
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── data/
│   ├── airline_safety.csv
    └── airline_safety.csv
├── myLib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── AirlineSafetyDB.db
├── main.py
├── Makefile
├── query_log.md
├── query_output.md
├── README.md  
├── ServeTimesDB.db  requirements.txt
└── test_main.py
```
## CRUD operations : 

## Usage

Run the script using the following command:

```python
python main.py <action> [arguments]
```
## Arguments: 

`record_id`, `airline`, `avail_seat_km_per_week`, `incidents_85_99`, `fatal_accidents_85_99`, `fatalities_85_99`, `incidents_00_14`, `fatal_accidents_00_14`, `fatalities_00_14`

## Actions:

extract: Extract data from the source.

```python
python main.py extract
```
transform_load: Transform and load data into the database.

```python
python main.py transform_load
```
update_record: Update an existing record in the database.

```python
python main.py update_record(1, "Air Canada", 2000000000, 3, 1, 5, 2, 0, 0)
```
create_record: Create a new record in the database

```python
python main.py create_record("Air Canada", 1865253802, 2, 0, 0, 2, 0, 0)
```
delete_record: delete an existing record in the database.

```python
python main.py delete_record(1)
```
read_data: Read and display the top N rows from the database.

```python
python main.py read_data(10)  # Reads the top 10 rows
```
general_query: Run a custom SQL query on the database.

```python
python main.py "SELECT * FROM AirlineSafety WHERE airline = 'Aeroflot*'"
```

## Testing
To run the test suite, use:

```python
python -m pytest -vv --cov=main --cov=myLib test_*.py
```
## References 
https://github.com/nogibjj/sqlite-lab