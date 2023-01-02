import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import shutil
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()

driver.get('https://stats.govt.nz/large-datasets/csv-files-for-download/')

# Wait for the element to be present on the page
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Annual enterprise survey: 2021 financial year')))

button.click()

url = driver.current_url

# Make an HTTP GET request to download the file
response = requests.get(url)

# Construct the full path to the file
# base_path = os.path.expanduser('~/PycharmProjects/adeelbhai')
# file_name = 'file1.csv'
# full_path = os.path.join(base_path, file_name)

# Save the file to disk
# with open('file.csv', 'wb') as f:
#     f.write(response.content)

driver.close()

#
time.sleep(5)
#
# Construct the full path to the file
base_path = '/home/afaq/Downloads'
file_name = 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
full_path = os.path.join(base_path, file_name)
print(full_path)
#
# # Copy the file from the source location to the destination location and preserve the metadata
shutil.copy(full_path, '/home/afaq/PycharmProjects/adeelbhai/file1.csv')
#################################################################################################################
# Read the CSV file into a pandas DataFrame
# Set the plot style to '_mpl-gallery'
plt.style.use('_mpl-gallery')

df = pd.read_csv('data.csv')

# Select the data to plot
x = df['total_rooms']
y = df['total_bedrooms']

# Plot the data
plt.plot(x, y)

# Add a title and axis labels
plt.title('Rooms & Bedrooms')
plt.xlabel('total_rooms')
plt.ylabel('total_bedrooms')

# Save the plot to an image file
plt.savefig('RoomsLinesplot.png')
