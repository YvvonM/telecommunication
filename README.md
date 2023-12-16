- [Data_retrieval](#Dataretrival)
- [Analysis](#analysis)


# Data retrieval
# Telecom Data Extraction and Export from postgreSQL
This Python script connects to a PostgreSQL database, runs a SQL query to retrieve data, then converts the data to a Pandas DataFrame and exports it to a CSV file.

## Requirements

Make sure you have the following installed before executing the script:

> - Python
> - PostgreSQL 

Python packages required:
> - sqlalchemy
> - pandas

1. To run the script, you need to update your database betails

    ```python
    # Database connection details
    username = 'your_postgres_username'
    password = 'your_postgres_password'
    host = 'localhost'
    port = '5432'
    database = 'your_database_name'
    ```
 ## analysis 
 
### Telecommunication data analysis
###### INTRODUCTION 

The goal of this project is to analyze telecom data in order to find patterns and significant insights that will help with business decision-making

##### OBJECTIVE

Our goal is to find trends, patterns, and important metrics via data manipulation, feature engineering, and visualization. These findings can help guide strategic decisions.

#### Installation
To run this code, you need to install the 'requirement.txt file'. Run it using
```
pip install -r requirements.txt
```

####  project structure
**Data Exploration**
> - Checked the shape, missing values, data types, and duplicates in the dataset.
> - Explored the statistical summary of both numeric and text columns.

**Exploratory data analysis**
> - Visualized columns to show types of handsets used by users, types of manufacturers of handsets, correlation, e.t.c

**Feature Engineering**
> - Removed missing values
> - Added new features to the datast
> - Scaled the data

**Model Building**
> - used unsupervised learning on the data
> - clustered the data using KMeans

##### Implementation
To run the code step-by-step, launch the jupyter notebook *telecom.ipynb*. 

