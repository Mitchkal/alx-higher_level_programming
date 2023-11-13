#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const [, , arg1, arg2] = process.argv;

console.log(add(arg1, arg2));
