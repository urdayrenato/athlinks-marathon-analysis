# Athlinks Marathon Analysis

Reusable Python pipeline for extracting, processing and analyzing marathon race results from Athlinks public result endpoints.

---

## Overview

This project automates the extraction and transformation of marathon race results published on Athlinks.

The pipeline was designed to:

- consume paginated JSON endpoints
- download raw race result datasets
- process and normalize structured data
- generate analytical CSV datasets
- support reusable extraction for multiple race distances (10K, 21K, 42K)

The project combines concepts from:

- lightweight data engineering
- ETL pipelines
- process automation
- analytics workflows
- API-based data extraction

---

## Technologies Used

- Python
- Requests
- Pandas
- PowerShell
- JSON APIs
- Git / GitHub

---

## Main Features

### 1. Automated JSON Extraction

The script consumes Athlinks public result endpoints and automatically downloads paginated race results.

Capabilities:

- paginated extraction
- bulk result download
- offset handling
- raw JSON export
- reusable event configuration

---

### 2. Data Processing and Transformation

The processing pipeline extracts and normalizes:

- overall rankings
- gender rankings
- age category rankings
- athlete information
- official finish times
- timing metrics

Includes:

- duplicate removal
- time normalization
- CSV export
- analytical dataset generation

---

## Project Structure

```text
athlinks-marathon-analysis/
│
├── data/
│   └── raw/
│       ├── 10k/
│       ├── 21k/
│       └── 42k/
│
├── outputs/
│
├── scripts/
│   ├── download_json.py
│   └── process_results.py
│
├── requirements.txt
└── README.md
```

---

## Pipeline Flow

```text
Athlinks Endpoint
        ↓
JSON Extraction
        ↓
Raw File Storage
        ↓
Data Processing
        ↓
Structured Dataset
        ↓
CSV Export
```

---

## Reusing the Pipeline for Another Race

The extraction script is reusable for different races hosted on Athlinks.

To use another race, update the following variables inside:

```text
scripts/download_json.py
```

### Parameters

```python
EVENT_ID = 447223
EVENT_COURSE_ID = 668417
TOTAL_ATHLETES = 11308
```

### Description

| Variable | Description |
|---|---|
| EVENT_ID | Main Athlinks event identifier |
| EVENT_COURSE_ID | Specific race distance/category identifier |
| TOTAL_ATHLETES | Total number of athletes to download |

Examples of race categories:

- 10K
- 21K Half Marathon
- 42K Marathon

---

## Example Usage

### 1. Download raw JSON results

```bash
python scripts/download_json.py
```

### 2. Process downloaded JSON files

```bash
python scripts/process_results.py
```

---

## Generated Outputs

The pipeline generates:

- raw JSON files
- structured CSV datasets
- normalized timing information
- ranking datasets ready for analysis

---

## Learning Objectives Applied

This project applies concepts related to:

- ETL pipelines
- process automation
- API consumption
- structured data transformation
- analytics engineering
- reusable scripting
- lightweight data engineering

---

## About This Project

This repository was developed as a personal technical initiative combining endurance sports analytics and lightweight data engineering workflows.

---

## Author

Renato Urday Calcina

Industrial Engineer | Process Analyst | BPM & Process Architecture | Runner | Data Analytics