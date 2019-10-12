from flask import Flask, send_file, request
from bs4 import BeautifulSoup
import json
import requests


app = Flask(__name__)

def scraper(query):
    url_list = []
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
            url_list.append('https://news.google.com/{}'.format(raw[i]))
        except IndexError:
            # Comment plez
            url_list.append('https://news.google.com/{}'.format(raw[i]))
        i += 1

    for q in range(12):
        url_list.pop(0)

    return tuple(url_list)

def createjson(st):
    x = json.dumps(st)
    with open("data.json", "w") as write_file:
        json.dump(x, write_file)
    print(json.dumps(x))



@app.route('/getinfo', methods=['GET'])
def getInfo(loc=None, top=None):
    output = scraper("homeless%20boston")

    for url in lis:
        summaries = SummarizeUrl(url)

    ret=createjson(summaries)

    #loc, topic
    #art

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return ret