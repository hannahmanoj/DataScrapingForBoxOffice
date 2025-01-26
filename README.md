# Box Office International Performance Tracker
## Overview
This project is a Python-based web scraping and data analysis tool designed to extract and analyze international box office performance data from Box Office Mojo. It automates the collection of key metrics such as weekend grosses, top releases, distributors, and regional performance, consolidating the information into a structured CSV format for further analysis.
## Features
- Automated Web Scraping: Uses BeautifulSoup and Requests to dynamically scrape data from a target URL.
- Data Extraction and Transformation: Extracts key metrics like area, weekend grosses, top releases, and distributors, transforming the unstructured data into a clean format.
- CSV Export: Organizes and saves the data in a CSV file using pandas for easy sharing and further analysis.
- Error Handling: Includes robust error handling to ensure stability during data scraping.
- Dynamic Links: Extracts and stores direct links for more detailed data exploration.

## Technologies Used
- Programming Language: Python
- Libraries: BeautifulSoup, Requests, pandas, CSV
- Tools: GitHub for version control

## Usage
- Run the script to fetch the latest box office data.
- The output will be saved as box_office_data.csv in the project directory.
- Open the CSV file to explore the data or use it for visualization and analysis.
