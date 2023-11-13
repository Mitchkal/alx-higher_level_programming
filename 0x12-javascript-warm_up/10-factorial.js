#!/usr/bin/node

const a = parseInt(process.argv[2], 10);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  } else if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(a));
