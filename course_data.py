#!/usr/bin/env python3
import sys
import re
import json
from datetime import datetime
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup


course_list_home_url = 'https://courselist.wm.edu/courselist'
course_list_url = 'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code={term_code}&' +\
                  'term_subj={subject}&attr=0&attr2=0&levl=0&status=0&ptrm=0&search=Search'


def get_course_data() -> Dict[str, Any]:
    r = requests.get(course_list_home_url)
    home_soup = BeautifulSoup(r.text, 'html.parser')
    terms = list_terms(home_soup)
    out = {}
    for term_name, term_code in terms.items():
        print('fetching term: {}'.format(term_name), file=sys.stderr)
        print('---------------------------', file=sys.stderr)
        out[term_name] = {}
        subjects = list_subjects(home_soup)
        for subject in subjects:
            print(subject['subject_name'], file=sys.stderr)
            out[term_name][subject['subject_name']] = {}
            url = course_list_url.format(term_code=term_code, subject=subject['subject_id'])
            r = requests.get(url)
            soup = BeautifulSoup(normalize_markup(r.text), 'html.parser')
            table = find_result_table(soup)
            columns = get_column_names(table)
            courses = parse_table(table, columns)
            for course in courses:
                course['MEET DAYS'] = list(filter(lambda x: x.strip(), list(course['MEET DAYS'])))
                course['CRSE ATTR'] = list(map(lambda x: x.strip(), course[' CRSE ATTR'].split(',')))
                del course[' CRSE ATTR']
                if course['MEET TIMES'].strip():
                    start, end = course['MEET TIMES'].split('-')
                    start_time = datetime(1, 1, 1, int(start[:2]), int(start[2:]))
                    end_time = datetime(1, 1, 1, int(end[:2]), int(end[2:]))
                    course['startTime'] = (start_time - datetime(1, 1, 1)).seconds * 1000
                    course['endTime'] = (end_time - datetime(1, 1, 1)).seconds * 1000
                subj, level, section, _ = course['COURSE ID'].split(' ')
                course['dept'] = subj
                course['level'] = level
                course['section'] = section
                if level in out[term_name][subject['subject_name']]:
                    out[term_name][subject['subject_name']][level][section] = course
                else:
                    out[term_name][subject['subject_name']][level] = {section: course}
    return out


def normalize_markup(html: str) -> str:
    html = re.sub(r'<tbody>\s*<td>', '<tbody><tr><td>', html)
    html = re.sub(r'</tr>\s*<td>', '</tr><tr><td>', html)
    return html


def get_column_names(table: BeautifulSoup) -> List[str]:
    out = []
    header = table.find('thead').find('tr')
    for column in header.find_all('th'):
        if 'class' in column.attrs and 'sortable' in column.attrs['class']:
            out.append(column.find('a').string)
        else:
            out.append(column.string)
    return out


def parse_table(table: BeautifulSoup, columns: List[str]) -> List[Dict[str, str]]:
    out = []
    tbody = table.find('tbody')
    for row in tbody.find_all('tr'):
        data = {}
        for i, entry in enumerate(row.find_all('td')):
            col = columns[i]
            if entry.find('a'):
                data[col] = entry.find('a').string
            else:
                data[col] = entry.string
        out.append(data)
    return out


def find_result_table(soup: BeautifulSoup) -> BeautifulSoup:
    return soup.find('table')


def list_subjects(soup: BeautifulSoup) -> List[Dict[str, str]]:
    out = []
    form_divs = soup.find_all('div', {'class': 'phoneHeader'})
    for field in form_divs:
        if field.find('p1').string == 'Subject':
            select = field.find('select')
            options = select.find_all('option')
            for option in options[1:]:
                out.append({
                    'subject_name': option.string,
                    'subject_id': option.attrs['value']
                })
            break

    return out


def list_terms(soup: BeautifulSoup) -> Dict[str, str]:
    out = {}
    form_divs = soup.find_all('div', {'class': 'phoneHeader'})
    for field in form_divs:
        if field.find('p1').string == 'Term':
            select = field.find('select')
            options = select.find_all('option')
            for option in options:
                out[option.string] = option.attrs['value']
            break
    return out


if __name__ == '__main__':
    classes = get_course_data()
    print(json.dumps(classes))
