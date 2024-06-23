#!/usr/bin/node
const oldList = require('100-data.js').list;

const newList = oldList.map((elem, indx) => elem * indx);

console.log(oldList);
console.log(newList);
