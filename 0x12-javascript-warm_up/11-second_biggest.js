#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
}

let biggest = parseInt(process.argv[2]);
let secondRunner;

for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > biggest) {
    secondRunner = biggest;
    biggest = parseInt(process.argv[i]);
    continue;
  }
  if (isNaN(secondRunner) || parseInt(process.argv[i]) > secondRunner) {
    secondRunner = parseInt(process.argv[i]);
  }
}
console.log(secondRunner);
