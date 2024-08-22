#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2], (error, res, body) => {
  if (error) {
    console.log(error);
  }
  const todoList = JSON.parse(body);
  const TODONUM = todoList.length;
  const dict = {};
  for (let i = 0; i < TODONUM; i++) {
    if (todoList[i].completed) {
      if (todoList[i].userId in dict) {
        dict[todoList[i].userId]++;
      } else {
        dict[todoList[i].userId] = 1;
      }
    }
  }
  console.log(dict);
});
