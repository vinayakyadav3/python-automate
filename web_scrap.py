import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://example.com')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract information from the parsed content
title = soup.title.text
links = soup.find_all('a')

# Print the extracted data
print("Title:", title)
print("Links:")

for link in links:
print(link.get('href'))
