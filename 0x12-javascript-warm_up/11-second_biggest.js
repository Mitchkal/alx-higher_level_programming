#!/usr/bin/node
const arrayNum = process.argv.slice(2);
function secondBig (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((i, j) => i - j);
    array.pop();
    return (array.pop());
  }
}
console.log(secondBig(arrayNum));
