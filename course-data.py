import urllib
import urllib2
from bs4 import BeautifulSoup
import json
import sys

semesters = {
    'spring2016': 201620
}

def main():
    term_code = semesters['spring2016'] # default to spring 2016

    if len(sys.argv) > 1:
        if sys.argv[1] not in semesters:
            print('Semesters not available')
            return
        else:
            term_code = sys.argv[1]

    FORM_DATA = {
        'term_code': 201620,
        'term_subj': 0,
        'attr': 0,
        'attr2': 0,
        'levl': 0,
        'status': 0,
        'ptrm': 0,
        'search': 'Search'
    }

    URL = 'https://courselist.wm.edu/courselist/courseinfo/searchresults'

    data = urllib.urlencode(FORM_DATA)
    req = urllib2.Request(URL, data)
    response = urllib2.urlopen(req)
    html = response.read()

    html = html.replace('</tr>', '')
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    c = 0
    col = {}
    cells = soup.find('tbody').find_all('td')
    for cell in cells:
        c += 1
        if c == 1:
            a = cell.find('a')
            col['crn'] = a.contents[0]
        elif c == 2:
            info = cell.contents[0].split(' ')
            col['department'] = info[0]
            col['courseId'] = info[1]
            col['section'] = info[2]
        elif c == 3:
            col['attr'] = cell.contents[0]
        elif c == 4:
            col['title'] = cell.contents[0]
        elif c == 5:
            col['instructor'] = cell.contents[0]
        elif c == 6:
            col['creditHours'] = cell.contents[0]
        elif c == 7:
            col['meetDays'] = cell.contents[0]
        elif c == 8:
            col['meetTimes'] = cell.contents[0]
        elif c == 10:
            col['currEnr'] = cell.contents[0]
        elif c == 11:
            col['seatsAvail'] = cell.contents[0]
        elif c == 12:
            col['status'] = cell.contents[0]
            c = 0
            data.append(col)
            col = {}

    print(json.dumps(data))

if __name__ == '__main__':
    main()
