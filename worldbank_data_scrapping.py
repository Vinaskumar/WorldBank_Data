# -*- coding: utf-8 -*-

!apt-get update
!apt-get install -y chromium-chromedriver
!apt-get install -y webdriver-manager
!pip install selenium
!pip install requests webdriver-manager

"""Scrape list of countries"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://data.worldbank.org/country'

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
download_dir = "world_bank_data"
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get(url)

# Give some time for the page to load completely
time.sleep(5)

countries_list = []

# Find the relevant sections containing country names
sections = driver.find_elements(By.CSS_SELECTOR, 'div#main div.overviewArea.body section')
print("Sections found:", len(sections))

for section in sections:
    items = section.find_elements(By.CSS_SELECTOR, 'ul li a')
    for item in items:
        country_name = item.text.strip()
        #print(country_name)
        countries_list.append([country_name])

print(countries_list)

"""Scrape data of each countries"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
import shutil

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
download_dir = "world_bank_data"
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

def download_excel(country_code, country_name):
    base_url = "https://databank.worldbank.org/reports.aspx"
    params = {
        "source": "2",
        "country": country_code
    }
    url = f"{base_url}?source={params['source']}&country={params['country']}"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    try:
        # Click on the "Download options" link to reveal the dropdown menu
        download_options_button = driver.find_element(By.CSS_SELECTOR, 'li.download a[data-toggle]')
        download_options_button.click()
        time.sleep(2)  # Wait for the dropdown menu to appear

        # Click on the "Excel" option in the dropdown menu
        excel_download_link = driver.find_element(By.CSS_SELECTOR, 'a[data-trackaction="Excel"]')
        excel_download_link.click()
        time.sleep(10)  # Wait for the download to complete

        print(f"Downloaded {country_name}")

        files = sorted(os.listdir(download_dir), key=lambda x: os.path.getctime(os.path.join(download_dir, x)))
        latest_file = os.path.join(download_dir, files[-1])
        new_file_name = os.path.join(download_dir, f"{country_code}.xlsx")
        shutil.move(latest_file, new_file_name)
        print(f"Moved {country_name} to {new_file_name}")

    except Exception as e:
        print(f"Failed to download file for {country_name}: {e}")

# List of countries and their codes
countries = {
    "AFG": "Afghanistan", "ALB": "Albania", "DZA": "Algeria", "ASM": "American Samoa",
    "AND": "Andorra", "AGO": "Angola", "ATG": "Antigua and Barbuda", "ARG": "Argentina",
    "ARM": "Armenia", "ABW": "Aruba", "AUS": "Australia", "AUT": "Austria",
    "AZE": "Azerbaijan", "BHS": "Bahamas, The", "BHR": "Bahrain", "BGD": "Bangladesh",
    "BRB": "Barbados", "BLR": "Belarus", "BEL": "Belgium", "BLZ": "Belize",
    "BEN": "Benin", "BMU": "Bermuda", "BTN": "Bhutan", "BOL": "Bolivia",
    "BIH": "Bosnia and Herzegovina", "BWA": "Botswana", "BRA": "Brazil", "BRN": "Brunei Darussalam",
    "BGR": "Bulgaria", "BFA": "Burkina Faso", "BDI": "Burundi", "CPV": "Cabo Verde",
    "KHM": "Cambodia", "CMR": "Cameroon", "CAN": "Canada", "CYM": "Cayman Islands",
    "CAF": "Central African Republic", "TCD": "Chad", "CHL": "Chile", "CHN": "China",
    "COL": "Colombia", "COM": "Comoros", "COD": "Congo, Dem. Rep.", "COG": "Congo, Rep.",
    "CRI": "Costa Rica", "CIV": "Cote d'Ivoire", "HRV": "Croatia", "CUB": "Cuba",
    "CUW": "Curacao", "CYP": "Cyprus", "CZE": "Czech Republic", "DNK": "Denmark",
    "DJI": "Djibouti", "DMA": "Dominica", "DOM": "Dominican Republic", "ECU": "Ecuador",
    "EGY": "Egypt, Arab Rep.", "SLV": "El Salvador", "GNQ": "Equatorial Guinea", "ERI": "Eritrea",
    "EST": "Estonia", "SWZ": "Eswatini", "ETH": "Ethiopia", "FJI": "Fiji",
    "FIN": "Finland", "FRA": "France", "GAB": "Gabon", "GMB": "Gambia, The",
    "GEO": "Georgia", "DEU": "Germany", "GHA": "Ghana", "GIB": "Gibraltar",
    "GRC": "Greece", "GRL": "Greenland", "GRD": "Grenada", "GUM": "Guam",
    "GTM": "Guatemala", "GIN": "Guinea", "GNB": "Guinea-Bissau", "GUY": "Guyana",
    "HTI": "Haiti", "HND": "Honduras", "HKG": "Hong Kong SAR, China", "HUN": "Hungary",
    "ISL": "Iceland", "IND": "India", "IDN": "Indonesia", "IRN": "Iran, Islamic Rep.",
    "IRQ": "Iraq", "IRL": "Ireland", "IMN": "Isle of Man", "ISR": "Israel",
    "ITA": "Italy", "JAM": "Jamaica", "JPN": "Japan", "JOR": "Jordan",
    "KAZ": "Kazakhstan", "KEN": "Kenya", "KIR": "Kiribati", "PRK": "Korea, Dem. People's Rep.",
    "KOR": "Korea, Rep.", "KWT": "Kuwait", "KGZ": "Kyrgyz Republic", "LAO": "Lao PDR",
    "LVA": "Latvia", "LBN": "Lebanon", "LSO": "Lesotho", "LBR": "Liberia",
    "LBY": "Libya", "LIE": "Liechtenstein", "LTU": "Lithuania", "LUX": "Luxembourg",
    "MAC": "Macao SAR, China", "MDG": "Madagascar", "MWI": "Malawi", "MYS": "Malaysia",
    "MDV": "Maldives", "MLI": "Mali", "MLT": "Malta", "MHL": "Marshall Islands",
    "MRT": "Mauritania", "MUS": "Mauritius", "MEX": "Mexico", "FSM": "Micronesia, Fed. Sts.",
    "MDA": "Moldova", "MCO": "Monaco", "MNG": "Mongolia", "MNE": "Montenegro",
    "MAR": "Morocco", "MOZ": "Mozambique", "MMR": "Myanmar", "NAM": "Namibia",
    "NRU": "Nauru", "NPL": "Nepal", "NLD": "Netherlands", "NCL": "New Caledonia",
    "NZL": "New Zealand", "NIC": "Nicaragua", "NER": "Niger", "NGA": "Nigeria",
    "MKD": "North Macedonia", "MNP": "Northern Mariana Islands", "NOR": "Norway", "OMN": "Oman",
    "PAK": "Pakistan", "PLW": "Palau", "PAN": "Panama", "PNG": "Papua New Guinea",
    "PRY": "Paraguay", "PER": "Peru", "PHL": "Philippines", "POL": "Poland",
    "PRT": "Portugal", "PRI": "Puerto Rico", "QAT": "Qatar", "ROU": "Romania",
    "RUS": "Russian Federation", "RWA": "Rwanda", "KNA": "Saint Kitts and Nevis", "LCA": "Saint Lucia",
    "VCT": "Saint Vincent and the Grenadines", "WSM": "Samoa", "SMR": "San Marino", "STP": "Sao Tome and Principe",
    "SAU": "Saudi Arabia", "SEN": "Senegal", "SRB": "Serbia", "SYC": "Seychelles",
    "SLE": "Sierra Leone", "SGP": "Singapore", "SXM": "Sint Maarten (Dutch part)", "SVK": "Slovakia",
    "SVN": "Slovenia", "SLB": "Solomon Islands", "SOM": "Somalia", "ZAF": "South Africa",
    "SSD": "South Sudan", "ESP": "Spain", "LKA": "Sri Lanka", "SDN": "Sudan",
    "SUR": "Suriname", "SWE": "Sweden", "CHE": "Switzerland", "SYR": "Syrian Arab Republic",
    "TWN": "Taiwan, China", "TJK": "Tajikistan", "TZA": "Tanzania", "THA": "Thailand",
    "TLS": "Timor-Leste", "TGO": "Togo", "TON": "Tonga", "TTO": "Trinidad and Tobago",
    "TUN": "Tunisia", "TUR": "Turkey", "TKM": "Turkmenistan", "TUV": "Tuvalu",
    "UGA": "Uganda", "UKR": "Ukraine", "ARE": "United Arab Emirates", "GBR": "United Kingdom",
    "USA": "United States", "URY": "Uruguay", "UZB": "Uzbekistan", "VUT": "Vanuatu",
    "VEN": "Venezuela, RB", "VNM": "Vietnam", "VIR": "Virgin Islands (U.S.)", "PSE": "Palestine",
    "YEM": "Yemen, Rep.", "ZMB": "Zambia", "ZWE": "Zimbabwe",
    "VGB": "British Virgin Islands", "CHI": "Channel Islands", "FRO": "Faroe Islands",
    "PYF": "French Polynesia", "XKX": "Kosovo", "MAF": "Saint Martin (French part)",
    "TCA": "Turks and Caicos Islands"
}

# Download Excel files for each country
for country_code, country_name in countries.items():
    download_excel(country_code, country_name)

driver.quit()

!zip -r world_bank_data.zip world_bank_data

"""Combine all files into one file"""

import pandas as pd
import os

output_filename = "world_bank_data_combined.xlsx"
first_file = True

with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
  for filename in os.listdir("world_bank_data"):
    if filename.endswith(".xlsx"):
      filepath = os.path.join("world_bank_data", filename)
      df = pd.read_excel(filepath)

      # Find the first blank row and slice the DataFrame
      blank_row_index = df[df.isnull().all(axis=1)].index.tolist()
      if blank_row_index:
        df = df.iloc[:blank_row_index[0]]

      if first_file:
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        first_file = False
      else:
        df.to_excel(writer, sheet_name="Sheet1", index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
