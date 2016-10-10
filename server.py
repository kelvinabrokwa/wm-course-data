#!/usr/bin/env python3.5
import sys
sys.path.append('.')
import os
import json
import redis
from flask import Flask
<<<<<<< HEAD
from flask_cors import CORS
from flask_compress import Compress
=======
from flask_cors import CORS, cross_origin
>>>>>>> 0aa9bd8c42cc122420b6ce801495cbfe8c42512b
from course_data import get_course_data


# Flask app
app = Flask(__name__)
CORS(app)
<<<<<<< HEAD
Compress(app)
=======
>>>>>>> 0aa9bd8c42cc122420b6ce801495cbfe8c42512b

# Redis
r = redis.from_url(os.environ.get("REDIS_URL"))

if r.get('courses') is None:
    r.set('courses', json.dumps(get_course_data()))

@app.route('/courses')
def courses():
    # Todo: check for data staleness
    return r.get('courses')
