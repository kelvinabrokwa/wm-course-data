#!/usr/bin/env python3.5
import sys
sys.path.append('.')
import os
import json
import redis
import requests
import urllib.parse
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from flask_compress import Compress
from course_data import get_course_data

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Flask app
app = Flask(__name__)
CORS(app)
Compress(app)


# Redis
r = redis.from_url(os.environ.get('REDIS_URL'))


if r.get('courses') is None:
    print('Fetching courses...')
    r.set('courses', json.dumps(get_course_data()))


@app.route('/courses')
def courses():
    # Todo: check for data staleness
    return jsonify(**json.loads(r.get('courses').decode('utf-8')))


@app.route('/geocode/<semester>/<crn>')
def geocode_section(semester, crn):
    req = requests.get('https://courselist.wm.edu/courselist/courseinfo/addInfo?fterm={term}&fcrn={crn}'.format(term=semester, crn=crn))
    soup = BeautifulSoup(req.text, 'html.parser')
    tables = soup.find_all('table')

    if len(tables) != 2:
        return jsonify(**{'err': 'no results'})

    rows = tables[1].find_all('tr')

    if len(rows) < 2:
        return jsonify(**{'err': 'no results'})

    building = rows[2].find_all('td')[1].get_text().split('--')[0]

    building_name = building

    if building == 'Small Physics Lab':
        building = 'Small Hall'
    elif building == 'Phi Beta Kappa Hall':
        building = '601 Jamestown Rd, Williamsburg, VA 23185'

    data = r.get(building_name)

    if data is not None:
        return jsonify(**json.loads(data.decode('utf-8')))

    params = urllib.parse.urlencode({
        'address': '{building}, Williamsburg, VA'.format(building=building),
        'key': GOOGLE_API_KEY
    })

    url = 'https://maps.googleapis.com/maps/api/geocode/json?{params}'.format(params=params)

    req = requests.get(url)

    if req.json()['status'] == 'ZERO_RESULTS':
        return jsonify(**{'err': 'no results'})

    coords = req.json()['results'][0]['geometry']['location']

    data = {'building': building_name, 'coords': coords}

    r.set(building_name, json.dumps(data))

    return jsonify(**data)
