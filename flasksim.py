import xml.etree.ElementTree as ET
from flask import Flask, render_template
import requests
import feedparser

THRUWAY = True
WEATHER = "NY"
RSS = ['http://feeds.bbci.co.uk/news/rss.xml?edition=us',
       'https://www.ncregister.com/feeds/general-news.xml']#,
#       'http://rss.slashdot.org/Slashdot/slashdotMainatom']

app = Flask(__name__)

@app.route("/")
def main():
    #print(request.headers)
    return render_template('ticker.html')

def get_thruway():
    tree = ET.fromstring(requests.get("https://www.thruway.ny.gov/xml/netdata/dmsstatus.xml").content)
    signs = {x.attrib['sign-text-1'].replace('~', ' ').strip() + ' ' + x.attrib['sign-text-2'].replace('~', ' ').strip() for x in tree.findall('dms')}
    signs.remove(' ')
    return [{'text': x.upper()} for x in signs]

def get_weather(state):
    weather = requests.get("https://api.weather.gov/alerts/active", params={'area': state}).json()
    events = {x['properties']['event'] for x in weather['features']}
    return [{'text': x.upper()} for x in events]

def get_rss(urls):
    feeds = [feedparser.parse(x) for x in urls]
    entries = []
    for feed in feeds:
        for entry in feed.entries:
            entries.append((entry.published_parsed, entry.title))
    return [{'text': x[1].upper()} for x in sorted(entries, reverse=True)][:3]

@app.route("/board")
def render_board():
    messages = []
    if THRUWAY:
        messages = messages + get_thruway()
    if WEATHER:
        messages = messages + get_weather(WEATHER)
    if RSS:
        messages = messages + get_rss(RSS)
    return {'messages': messages}

