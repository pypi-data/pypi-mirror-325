# Weather Data Loading and Analysis Project

## Overview
This project demonstrates how to load a dataset from a CSV file, process the data, and analyze it using Python and 
the `pandas` library. The dataset contains weather data from Australia, and the project includes functionality 
for calculating and displaying basic descriptive statistics 
as well as detailed statistics like mean, median, mode, and range.

## Objective
The goal of this project is to:
- Load the **Australia Weather Data** dataset from a CSV file.
- Use the `pandas` library to read and manipulate the data.
- Perform statistical analysis including basic and detailed statistics for numerical columns.
- Generate Python documentation using the `pydoc` tool, which automatically creates an HTML file describing the code's 
functions and methods.

## Features
- **DataLoader**: A class to load weather data from a CSV file into a pandas DataFrame.
- **DataProcessor**: A class to process the loaded data and calculate statistics such as mean, median, mode, and range.
- **WeatherAnalysis**: Orchestrates data loading and processing, and prints both general and detailed statistics.

## Steps Followed:
1. **Dataset**: 
   - The dataset `Australia Weather Data.csv` was downloaded from Kaggle. This dataset contains details about weather 
   conditions in Australia, including temperature, humidity, wind speed, and more.
   
2. **Python Code**: 
   - The dataset was loaded using the `pandas.read_csv()` function.
   - Descriptive statistics were generated using `pandas.DataFrame.describe()` for a general overview and custom 
   methods for detailed statistics like mean, median, mode, and range.

3. **Documentation**: 
   - The code was documented using Python's `pydoc` tool. This tool extracts the docstrings from the code and generates 
   a readable HTML documentation file, making it easier to understand and share.

## How to Run the Code:
1. **Install Dependencies**:
   Ensure that you have **Python** and **pandas** installed. If you don’t have pandas, you can install it using 
the following command:
   
   ```bash
   pip install pandas
   
2. **Download the Dataset**:
   Download the dataset from Australia Weather Data on Kaggle. Place the Weather Test Data.csv file in the same 
directory as the Python script (e.g., main3.py).

3. **Run the Python Script**:
   Open a terminal or command prompt.
Navigate to the folder where the Python script (main3.py) and the CSV file (Weather Test Data.csv) are located.
Run the script using the following command:

    ```bash
    python main3.py

4. **View Documentation**:
   - The Python code is documented using pydoc, and an HTML file
   - Open the generated HTML file in any browser to view the documentation:
   ```bash
   start weather_analysis_jory_3.html