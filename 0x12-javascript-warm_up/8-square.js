#!/usr/bin/node
let row = '';
if (process.argv[2] && parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let ii = 0; ii < parseInt(process.argv[2]); ii++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
} else {
  console.log('Missing size');
}
