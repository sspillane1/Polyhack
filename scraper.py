# Make sure these are installed
from bs4 import BeautifulSoup
import requests
from pyteaser import SummarizeUrl
from pprint import pprint

#
# class Scraper:
"""This is a scraper, but it only works for google news
                developed by David Kelchner            """



# def __init__(self, q):
# #     self.query = q


# Comment this stuff out
if __name__ == "__main__":
    # Use this Unicode format though or it will break Google
    query = "homelessness%20massachusetts"

    lis = scraper(query)

    urls = (u'https://ktvl.com/news/local/police-help-homeless-people-find-permanent-housing',
            u'http://www.bbc.co.uk/news/world-europe-30035666',
            u'http://www.bbc.co.uk/news/magazine-29631332')




    for url in lis:
        summaries = SummarizeUrl(url)
        pprint(summaries)
