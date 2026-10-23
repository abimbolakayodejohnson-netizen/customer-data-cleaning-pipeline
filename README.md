# Customer Data Cleaning Pipeline

## Project Overview
This project demonstrates an end-to-end customer data cleaning and validation pipeline built with Python and pandas. It uses a sample dataset containing inconsistent text, missing values, invalid ages, malformed email addresses, and duplicate customer records.

## Objectives
- Clean and standardize customer names and city names.
- Convert age values to numeric format.
- Validate customer names, ages, and email formatting.
- Detect duplicate email addresses.
- Generate a data-quality report.
- Export cleaned, validated, and duplicate records to CSV files.

## Tools and Technologies
- Python
- pandas
- CSV data files
- PyCharm

## Data Cleaning and Validation Steps
1. Remove unnecessary spaces and standardize name and city capitalization.
2. Convert ages to numeric values, coercing unconvertible values to missing values.
3. Validate ages against the range 0–120.
4. Apply basic email-format checks.
5. Flag missing or blank customer names.
6. Detect duplicate email addresses using normalized email values.
7. Generate data-quality metrics and export the results.

## Results
The sample dataset contained 8 customer records.

| Metric | Result |
|---|---:|
| Total records | 8 |
| Missing names | 1 |
| Missing ages | 2 |
| Missing emails | 1 |
| Invalid ages | 4 |
| Invalid emails | 3 |
| Invalid names | 2 |
| Valid ages | 50% |
| Valid emails | 62.5% |
| Duplicate records flagged | 2 |
| Duplicate percentage | 25% |

## Output Files
- `validated_df.csv` — cleaned records with validation flags.
- `unique_customers.csv` — records retained after duplicate detection.
- `duplicate_customers.csv` — records flagged as duplicate email entries.

**Note:** Retained records are not necessarily free of data-quality issues. They may still require review.

## How to Run
1. Install Python.
2. Install pandas using `python -m pip install pandas`.
3. Run `customer_cleaning.py`.
4. Review the printed report and generated CSV files.

## Limitations
- Email validation checks basic formatting only; it does not verify whether an email address exists.
- Duplicate detection uses email addresses and retains the first occurrence.
- The age range of 0–120 is an exercise-specific validation rule.
- The dataset is synthetic and intended for demonstration.

## Skills Demonstrated
Python functions, pandas DataFrames, data standardization, missing-value handling, type conversion, validation, duplicate detection, reporting, and CSV export.
