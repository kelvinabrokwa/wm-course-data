# wm-course-data

A microservice and library for fetching all course data available on the [William and Mary Open Course List](https://courselist.wm.edu/courselist) as well structured JSON.

Built for [Heroku](https://heroku.com/)


### Dependencies

- Python 3.5

Installing on Ubuntu

```sh
sudo apt-get install libssl-dev openssl -y
wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
tar xzvf Python-3.5.0.tgz
cd Python-3.5.0
./configure
make
sudo make install
```

- Redis

Make sure to set the `REDIS_URL` environment variable 

### Usage

To scrape course data from the command line:

```sh
git clone git@github.com:kelvinabrokwa/wm-course-data.git /opt/
cd /opt/wm-course-data
virtualenv -p python3.5 env
source env/bin/activate
pip install -r requirements.txt
./course-data.py
```

To start the service:

```sh
gunicorn server:app --timeout 120 # timeout gives worker enough time to scrape data
```

Course data will be available at `/courses`


**Output:** a JSON object of courses

```js
{
  "Spring 2017": {
    "Applied Science": {
      "401": {
        "01": {
          " CRSE ATTR": "  ",
          "COURSE ID": "APSC 401 01 ",
          "INSTRUCTOR": "Shaw, Leah",
          "MEET DAYS": "   ",
          "CRN": null,
          "PROJ ENR": "2",
          "CRDT HRS": "1",
          "TITLE": "Research Applied Science",
          "MEET TIMES": "  ",
          "CURR ENR": "0",
          "SEATS AVAIL": "2",
          "STATUS": "OPEN"
        }
      },
      "791": {
        "01": {
          " CRSE ATTR": "  ",
          "COURSE ID": "APSC 791 01 ",
          "INSTRUCTOR": "Smith, Gregory",
          "MEET DAYS": "TR ",
          "CRN": null,
          "PROJ ENR": "3",
          "CRDT HRS": "3",
          "TITLE": "Networks in Systems Biology",
          "MEET TIMES": "0930-1050",
          "CURR ENR": "0",
          "SEATS AVAIL": "6",
          "STATUS": "OPEN"
        }
      }
    }
  }
}
```
