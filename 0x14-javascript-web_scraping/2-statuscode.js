#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
