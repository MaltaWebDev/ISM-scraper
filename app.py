import requests
from bs4 import BeautifulSoup

url = 'https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi/february/'

# make a request to the webpage and get the HTML content
response = requests.get(url)
html_content = response.content

# create a Beautiful Soup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# initialize an empty dictionary to store the results
results = {}

# loop through each list item in the section and extract the text
for li in soup.find_all('li'):
    print(li)
    # extract the industry name from the square brackets
    industry = li.find('strong').text.strip('[]')
    # extract the text from the list item
    text = li.text.replace(industry, '').strip()
    # add the industry and text as a key-value pair to the results dictionary
    results[industry] = text

# print the results dictionary
print(results)

