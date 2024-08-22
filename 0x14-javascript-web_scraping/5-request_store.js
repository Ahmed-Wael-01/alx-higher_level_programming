#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const request = require('request');

request(process.argv[2], (error, res, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, err => {
    if (err) {
      console.log(err);
    }
  });
});
