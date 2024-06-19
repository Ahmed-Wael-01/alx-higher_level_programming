#!/usr/bin/node
const first = (process.argv[2]) ? process.argv[2] : 'undefined';
const second = (process.argv[3]) ? process.argv[3] : 'undefined';

console.log(`${first} is ${second}`);
