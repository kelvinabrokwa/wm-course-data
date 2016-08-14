#!/usr/bin/env node
const fs = require('fs');
const express = require('express');
const cors =  require('cors');
const exec = require('child_process').exec;

const app = express();
app.use(cors());

app.get('/courses', (req, res) => {
  fs.readFile('/opt/course_data.json', (err, data) => {
    if (err) {
      console.log(err);
      res.json({ error: 'no data available' });
      return;
    }
    res.json(JSON.parse(data));
  });
});

app.post('/courses/refresh', (req, res) => {
  exec('./course_data.py > /opt/course_data.json', (err, stdout, stderr) => {
    if (err) {
      console.log(err);
      res.send({ error: 'error scraping course data' });
      return;
    }
    res.send({ message: 'scraping course data' });
    console.log(stdout);
    console.log(stderr);
  });
});

app.listen(80, () => {
  console.log('Courses service listening at port: ' + '80');
});

