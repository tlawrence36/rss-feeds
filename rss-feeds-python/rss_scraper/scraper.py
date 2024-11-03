# scrape html from a url

import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract content

    title = soup.find('h1').text.strip()

    # TODO: container is going to vary based on site, so need a way to determine which to use
    container = soup.find('div', class_='FITT_Article_main__body') # ABC

    paragraphs = []
    # TODO: need to also extract headline (h2, h3?, ...?), so may need to change to read each line and extract
    # if it's a p, h2, h3, etc.
    for paragraph in container.find_all('p'):
        paragraphs.append(paragraph.text.strip())

    # Print the extracted data
    print("Title:", title)
    print("story:")
    for paragraph in paragraphs:
        print(paragraph)


scrape_url('https://abcnews.go.com/US/wireStory/halloween-means-time-bat-beauty-contest-115170107')