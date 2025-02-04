# The Shard Data Quality Check Package

The Shard Data Quality Check Package is a package to help automate data quality checks for a database before and after ETL and Injection into a database.

## Features

* Detect duplicates
* Identify missing values
* Compute five-number summary
* Validate schema using Pandera. Validation include checking if
  * Values are greater, less, great than or equal to, less than or equal to a specified value
  * If dates are before, after, before or on, after or on and between specified dates.
  * The min and max length
  * If there are nulls
  * if a specified value is in a specified list.

## Install

```
$ pip install data_quality_checks_the_shard
```
