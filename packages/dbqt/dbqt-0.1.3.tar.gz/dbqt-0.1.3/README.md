# DBQT (DataBase Quality Tool) 🎯

DBQT is a lightweight, Python-first data quality testing framework that helps data teams maintain high-quality data through automated checks and intelligent suggestions. 

## 🛠️ Current Tools

### Column Comparison Tool (dbqt compare)
Compare database schemas between source and target databases:
- Table-level comparison
- Column-level comparison with data type compatibility checks
- Generates detailed Excel report with:
  - Table differences
  - Column differences
  - Data type mismatches
  - Formatted worksheets for easy analysis

Usage:
```bash
dbqt compare source_schema.csv target_schema.csv
```

To generate the required CSV schema files from your database, run this query:
```sql
SELECT
    upper(table_schema) as sch,
    upper(table_name) as name,
    upper(column_name) as col_name,
    upper(data_type) as data_type,
    ordinal_position
FROM information_schema.columns
where table_schema = 'YOUR_SCHEMA'
order by table_name, ordinal_position;
```

Export the results to CSV format to use with the compare tool.

### Database Statistics Tool (dbqt dbstats)
Collect and analyze database statistics:
- Table row counts
- Updates statistics in CSV format
- Configurable through YAML

Usage:
```bash
dbqt dbstats config.yaml
```

Example config.yaml:
```yaml
# Database connection configuration
connection:
  type: mysql  # mysql, snowflake, duckdb, csv, parquet, s3parquet
  host: localhost
  user: myuser
  password: mypassword
  database: mydb
  # Optional AWS configs for s3parquet
  # aws_profile: default
  # aws_region: us-west-2
  # bucket: my-bucket

  # Snowflake-specific configs
  # type: snowflake
  # account: your_account.region
  # warehouse: YOUR_WAREHOUSE
  # database: YOUR_DB
  # schema: YOUR_SCHEMA
  # role: YOUR_ROLE
  # authenticator: externalbrowser  # Optional: use SSO authentication
  # user: your_username
  # password: your_password  # Not needed if using externalbrowser auth

# Path to CSV file containing table names to analyze
tables_file: tables.csv
```

The tables.csv file should contain at minimum a `table_name` column. The tool will add/update a `row_count` column with the results.

## 🚀 Future Plans

### Core DBQT Features (Coming Soon)
- AI-Powered column classification using Qwen2 0.5B
- Automatic check suggestions
- 20+ built-in data quality checks
- Python-first API
- No backend required
- Customizable check framework

### Planned Checks
- Completeness checks (null values)
- Uniqueness validation
- Format validation (regex, dates, emails)
- Range/boundary checks
- Value validation
- Statistical analysis
- Dependency checks

### Integration Plans
- Data pipeline integration
- Scheduled runs
- Parallel check execution
- Multiple database backend support

## 📄 License

This project is licensed under the MIT License.
