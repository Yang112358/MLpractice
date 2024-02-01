import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the webpage containing the data
url = 'http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the data (you might need to inspect the HTML structure)
    table = soup.find('table')

    # Extract data from the table into a pandas DataFrame
    df = pd.read_html(str(table))[0]

    # Save the DataFrame to a CSV file
    df.to_csv('heights_weights_data.csv', index=False)

    print('Data has been saved to heights_weights_data.csv')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")