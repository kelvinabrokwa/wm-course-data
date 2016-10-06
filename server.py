#!/usr/bin/env python3.5
import sys
sys.path.append('.')
import json
from flask import Flask
from course_data import get_course_data

app = Flask(__name__)

courses = None


@app.route('/courses')
def hello_world():
    global courses
    if courses is None:
        courses = get_course_data()
    return json.dumps(courses)
