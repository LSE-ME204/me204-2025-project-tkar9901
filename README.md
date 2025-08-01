[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tPsjfIAZ)

# Do certain Regions of England lag in Higher Education Performance compared to others?

This project will look on a Regional Scale at the disparities in Higher Education (16-18 Studies), focusing on Retention of students, breakdown by certain Characteristics and in particular a deeper dive into STEM uptake within the A level cohort.

## 🎯 Project Overview

This project demonstrates a complete data engineering pipeline from data collection to analysis and public communication. After collecting educational statistics from the Department of Education source EES (Explore Education Statistics), I designed and implemented a SQLite relational database, and conducted exploratory analysis to understand storytelling patterns.

## 📁 Project Structure

```
project-sample/
├── data/
│   ├── database.db             # SQLite database with processed data
│   └── raw/                    # Raw script data (CSV files)
├── docs/
│   ├── figures                 # Folder for all images
│   └── index.md                # Public website (main story)
├── notebooks/
│   ├── NB01_Data Collection.ipynb        # Script data collection
│   ├── NB02_Database_Collection.ipynb    # Database design & ETL
│   └── NB03_Data_Analysis.ipynb          # Exploratory analysis
├── README.md                   # This file
├── requirements.txt            # Packages required to run project
└── scripts/                    # Utility scripts
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Required packages: found in `requirements.txt` otherwise manually install the following:

```
Package    Version
---------- -------
ipykernel  6.30.0
matplotlib 3.10.3
pandas     2.3.1
pip        25.1.1
SQLAlchemy 2.0.41
```

### Installation
```bash
git clone [this-repo-url]
cd final_project
pip install -r requirements.txt
```
The `requirements.txt` file contains everything necessary for a virtual env. setup if you prefer that.

## 📊 Data Sources

This project uses Educational Data collected from  EES which is publicly available. The data includes 5 CSVs all covering various topics across 16-18 Studies attainment, retention, grades and more detailed datasets looking at stem subject combinations and student characteristics (gender, ethnicity etc.).

**Note:** No API credentials are required as this data was collected from publicly available sources.

## 🔄 Reproduction Workflow

To reproduce this analysis, follow these steps in order:

1. Data Collection (NB01)

    Open `NB01_Data_Collection.ipynb` and run all cells. This notebook collects the raw data, cleans & processes it into a usable format and saves it to `../data/raw/`.

2. Database Processing (NB02)

    Open `NB02_Database_Design.ipynb` and run all cells. This notebook reads raw data from `../data/raw/`, builds a SQLite database with proper schema, processes and cleans the data, and saves the database to `../data/database.db`.

3. Analysis (NB03)

    Open `NB03_Data_Analysis.ipynb` and run all cells. This notebook reads data from the SQLite database, creates visualisations and analysis, and generates insights about regional performance.

## 🗄️ Database Schema

The database schema and table structures are documented in `NB02_Database_Design.ipynb`. The SQLite database (`data/database.db`) contains tables for the 5 CSVs with appropriate relationships and data types.

## 📈 Key Findings

Have a look at this Github hosted website that documents my findings in an easily digestable way: [Project Website](https://lse-me204.github.io/me204-2025-project-tkar9901/).

Or you are welcome to look through the `NB03_Data_Analysis.ipynb` notebook to see a more detailed look through all my EDA and Analysis steps.

## 🚩 Verification

To verify the analysis is working, open `NB03_Data_Analysis.ipynb` and run all cells. This should generate the plots as described within.

## 📄 License

This project is for educational purposes as part of the ME204 course at LSE.

## 🤝 Contributing

This is a course project, but suggestions for improvements are welcome.

---

**Author:** Tamanna Kar  
**Course:** ME204 - Data Engineering for the Social World  
**Institution:** London School of Economics  
**Date:** July 2025