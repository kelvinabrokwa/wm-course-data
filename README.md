# wm-course-data

Download all course data available on the [W&M Open Course List](https://courselist.wm.edu/courselist) as well structured JSON.


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


### Usage

```
git clone git@github.com:kelvinabrokwa/wm-course-data.git
cd wm-course-data
pip install -r requirements.txt
./course-data.py
```


**Output:** a JSON object of courses printed to stdout

Sample output:

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
