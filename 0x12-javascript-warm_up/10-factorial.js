#!/usr/bin/node
function recfac (num) {
  if (isNaN(num) || num < 2) {
    return 1;
  }
  return recfac(num - 1) * num;
}

console.log(recfac(process.argv[2]));
