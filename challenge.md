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
- The extracted data is cleaned and structured into a uniform format. During this process, the following parameters were chosen to be included in the final cleaned dataset:

#### Population and Demographics
- Population, total
- Population growth (annual %)
- Urban population growth (annual %)
- Net migration
- Surface area (sq. km)

#### Economy and Finance
- GDP (current US$)
- Agriculture, forestry, and fishing, value added (% of GDP)
- Industry (including construction), value added (% of GDP)
- Exports of goods and services (% of GDP)
- Imports of goods and services (% of GDP)
- GDP growth (annual %)
- Tax revenue (% of GDP)
- Inflation, GDP deflator (annual %)
- Foreign direct investment, net inflows (BoP, current US$)
- Military expenditure (% of GDP)

#### Education
- School enrollment, primary (% gross)
- School enrollment, secondary (% gross)
- Primary completion rate, total (% of relevant age group)

#### Health
- Life expectancy at birth, total (years)
- Mortality rate, under-5 (per 1,000 live births)
- Immunization, measles (% of children ages 12-23 months)
- Prevalence of HIV, total (% of population ages 15-49)

#### Environment
- CO2 emissions (metric tons per capita)
- Forest area (sq. km)

#### Infrastructure
- Energy use (kg of oil equivalent per capita)
- Electric power consumption (kWh per capita)
- Mobile cellular subscriptions (per 100 people)

#### Governance
- Time required to start a business (days)

These indicators provide a comprehensive view of each country's demographic, economic, educational, health, environmental, infrastructure, and governance status.

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

## Running the Project

To run this project, you need an environment capable of executing Jupyter Notebook (`.ipynb`) files. You can either:

1. **Install Jupyter Notebook** locally on your machine and open the `.ipynb` files.

2. **Use Google Colab** directly in your web browser, which is a free and convenient option that requires no local installation. You can upload the notebooks to Colab and run them there.

Both options allow you to execute the code and view the visualizations included in the project.


## Additional Notes
- The project demonstrates skills in web scraping, data processing, API development, and data visualization.
- Future improvements could include more comprehensive metadata, enhanced API documentation, or additional data visualizations.
