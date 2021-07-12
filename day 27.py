# Import required modules
import requests
import bs4
import pandas as pd



# Make requests from webpage
url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)



# Creating soap object
soup = bs4.BeautifulSoup(result.text,'html.parser')



# Searching div tags having maincounter-number class
cases = soup.find_all('div' ,class_= 'maincounter-number')



# List to store number of cases
data = []

# Find the span and get data from it
for i in cases:
	span = i.find('span')
	data.append(span.string)

# Display number of cases
print(data)



# Creating dataframe
df = pd.DataFrame({"CoronaData": data})

# Naming the coloumns
df.index = ['TotalCases', ' Deaths', 'Recovered']



# Exporing data into Excel
df.to_excel('Corona_Data.xls')
