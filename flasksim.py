import random
import xml.etree.ElementTree as ET
from flask import Flask, render_template
import requests

THRUWAY = True
WEATHER = "NY"

app = Flask(__name__)

@app.route("/")
def main():
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


@app.route("/board")
def render_board():
    messages = []
    if THRUWAY:
        messages = messages + get_thruway()
    if WEATHER:
        messages = messages + get_weather(WEATHER)
    return {'messages': messages}

