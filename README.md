# wm-course-data

Download a semester's worth of William & Mary course data

### Usage

```
git clone git@github.com:kelvinabrokwa/wm-course-data.git
cd wm-course-data
python course-data.py
```

**Output** a JSON array of courses printed to stdout

Sample output:

```
[
  {
    "status":"OPEN",
    "attr":"C100",
    "creditHours":"4",
    "courseId":"AFST 100 03 ",
    "meetTimes":"1530-1650",
    "title":"How Rastafari Moved World",
    "meetDays":"MW ",
    "currEnr":"6",
    "instructor":"Osiapem, Iyabo",
    "crn":"24950",
    "seatsAvail":"19"
  },
  {
    "status":"OPEN",
    "attr":"C150, FRSM",
    "creditHours":"4",
    "courseId":"AFST 150 01 ",
    "meetTimes":"1530-1650",
    "title":"Intro to Africana Studies",
    "meetDays":"MW ",
    "currEnr":"5",
    "instructor":"Lott, Patricia",
    "crn":"24977",
    "seatsAvail":"10"
  },
  {
    "status":"CLOSED",
    "attr":"C200, CSI, GE4C, GE5",
    "creditHours":"3",
    "courseId":"AFST 205 03 ",
    "meetTimes":"1230-1350",
    "title":"Intro to Africana Studies",
    "meetDays":"TR ",
    "currEnr":"36",
    "instructor":"Vinson, Robert",
    "crn":"24194",
    "seatsAvail":"-6"
  },
  {
    "status":"CLOSED",
    "attr":"ALV, C200",
    "creditHours":"3",
    "courseId":"AFST 210 01 ",
    "meetTimes":"1530-1820",
    "title":"Medicine,  Arts,  Social Justice",
    "meetDays":"W ",
    "currEnr":"10",
    "instructor":"Braxton, Joanne",
    "crn":"25009",
    "seatsAvail":"0*"
  },
  {
    "status":"OPEN",
    "attr":"",
    "creditHours":"3",
    "courseId":"AFST 251 01 ",
    "meetTimes":"1400-1520",
    "title":"Caribbean Lang  &  Identity",
    "meetDays":"MW ",
    "currEnr":"7",
    "instructor":"Osiapem, Iyabo",
    "crn":"25073",
    "seatsAvail":"9"
  }
]
```
