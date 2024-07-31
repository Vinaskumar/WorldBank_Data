# World Bank Data Scraping and API Project

## Project Overview
This project involves web scraping data from the World Bank website, processing and cleaning the data, and providing an API using FastAPI to access country-specific information. It also includes various visualizations to demonstrate data analysis.

## Repository Structure

### [WorldBank_data_scrapping.ipynb](https://github.com/Vinaskumar/WorldBank_Data/blob/main/WorldBank_data_scrapping.ipynb)
This notebook contains the code for web scraping the World Bank website to obtain data for various countries. The scraping process includes extracting relevant information such as population, GDP, life expectancy, and more.

### [WorldBank_data_cleaning.ipynb](https://github.com/Vinaskumar/WorldBank_Data/blob/main/WorldBank_data_cleaning.ipynb)
This notebook details the data cleaning and transformation processes. The raw data obtained from scraping is cleaned and transformed into a structured format suitable for analysis and API usage.

### [WorldBank_data_visualization.ipynb](https://github.com/Vinaskumar/WorldBank_Data/blob/main/WorldBank_data_visualization.ipynb)
This notebook includes various visualizations created from the cleaned data. It explores relationships between different economic and social indicators across countries.

### [world_bank_data_cleaned.csv](https://github.com/Vinaskumar/WorldBank_Data/blob/main/world_bank_data_cleaned.csv)
The cleaned and processed data is stored in this CSV file. It contains relevant indicators for each country, prepared for use in the API and visualizations.

## Data and ETL Process

### Extract
- Data is extracted from the World Bank website using web scraping techniques.

### Transform
- The extracted data is cleaned and structured into a uniform format, removing inconsistencies and irrelevant information.

### Load
- The cleaned data is loaded into a CSV file [world_bank_data_cleaned.csv](https://github.com/Vinaskumar/WorldBank_Data/blob/main/world_bank_data_cleaned.csv) for easy access and analysis.

## API Instructions
To access country-specific data through the API:

1. Open the link provided for the API endpoint.
2. To get data for a specific country, add `/country/{country_name}` to the URL in your browser's address bar, replacing `{country_name}` with the name of the desired country.
   - Example: If the base URL is `http://your-api-url`, to get data for "France", navigate to `http://your-api-url/country/France`.
3. Hit enter to view the data.

## Visualizations
The project includes several visualizations that provide insights into global economic and social trends. These visualizations are created using libraries like Plotly and are available in the [WorldBank_data_visualization.ipynb](https://github.com/Vinaskumar/WorldBank_Data/blob/main/WorldBank_data_visualization.ipynb) notebook.

## Additional Notes
- The project demonstrates skills in web scraping, data processing, API development, and data visualization.
- Future improvements could include more comprehensive metadata, enhanced API documentation, or additional data visualizations.
