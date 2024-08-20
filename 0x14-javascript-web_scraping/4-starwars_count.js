#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2],
  (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const bodyList = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < bodyList.length; i++) {
      if (bodyList[i].characters.find(
        (character) => character.endsWith('/18/'))) {
        counter++;
      }
    }
    console.log(counter);
  });
