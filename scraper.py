# Make sure these are installed
from bs4 import BeautifulSoup
import requests

#
# class Scraper:
"""This is a scraper, but it only works for google news
                developed by David Kelchner            """


# def __init__(self, q):
#     self.query = q

def scraper(query):
    # Grab url of news site to be searched and add search query
    # Can add a switch statement if we want more sites
    url = "https://news.google.com/search?q={}&hl=en-US&gl=US&ceid=US%3Aen".format(query)
    response = requests.get(url)
    data = response.text
    browser = BeautifulSoup(data, 'lxml')
    # print(browser.get_text())
    raw = []
    # Generate array of only urls from page
    for link in browser.find_all('a'):
        if "./" in str(link.get('href')):
            raw.append(str(link.get('href')))
    # Check for dupes
    i = 0
    while i < len(raw):
        try:
            if raw[i] == raw[i + 1]:
                del raw[i]

            # Comment plez
            print("https://news.google.com/{}".format(raw[i]))
        except IndexError:
            # Comment plez
            print("https://news.google.com/{}".format(raw[i]))
        i += 1

#Comment this stuff out
if __name__ == "__main__":
    # Use this Unicode format though or it will break Google
    query = ""# "medford%20ma"
    scraper(query)
