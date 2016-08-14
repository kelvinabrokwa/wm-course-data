#!/usr/bin/env bin
import re
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup


course_list_home_url = 'https://courselist.wm.edu/courselist'
course_list_url = 'https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code=201710&term_subj={}&attr=0&attr2=0&levl=0&status=0&ptrm=0&search=Search'


def main() -> List[Dict[str, Any]]:
    r = requests.get(course_list_home_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    subjects = list_subjects(soup)
    out = []
    for subject in subjects[:1]:
        url = course_list_url.format(subject)
        r = requests.get(url)
        soup = BeautifulSoup(normalize_markup(r.text), 'html.parser')
        table = find_result_table(soup)
        columns = get_column_names(table)
        out += parse_table(table, columns)
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
            data[col] = entry.string
        out.append(data)
    return out


def find_result_table(soup: BeautifulSoup) -> BeautifulSoup:
    return soup.find('table')


def list_subjects(soup: BeautifulSoup) -> List[str]:
    out = []
    form_divs = soup.find_all('div', {'class': 'phoneHeader'})
    for field in form_divs:
        if field.find('p1').string == 'Subject':
            select = field.find('select')
            options = select.find_all('option')
            for option in options[1:]:
                out.append(option.attrs['value'])
            break

    return out


if __name__ == '__main__':
    classes = main()
    print(classes)
