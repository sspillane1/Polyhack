# Make sure these are installed
from bs4 import BeautifulSoup
import requests

"""This is a scraper, it takes in garbage and creates more garbage
                developed by David Kelchner            """


def scraper2(url):
    # Grab url of news site to be searched and add search query
    # Can add a switch statement if we want more sites
    response = requests.get(url)
    data = response.text
    browser = BeautifulSoup(data, 'lxml')
    # print(browser.get_text())
    raw = []
    # Generate array of only urls from page
    for par in browser.find_all('p'):
        raw.append(par)
    print(raw)
    return raw
#Comment this stuff out
if __name__ == "__main__":
    # Please send back a url or it will break :(
    url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup"
    scraper2(url)
