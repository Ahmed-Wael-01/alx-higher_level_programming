#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
}

let biggest = 2;
let secondRunner;

for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > parseInt(process.argv[biggest])) {
    secondRunner = biggest;
    biggest = i;
    continue;
  }
  if ((isNaN(secondRunner) ||
      parseInt(process.argv[i]) > parseInt(process.argv[secondRunner])) && i != biggest) {
    secondRunner = i;
  }
}
console.log(process.argv[secondRunner]);
