#!/usr/bin/node

const [, , count] = process.argv;

const times = parseInt(count);
let x = 0;

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (x = times; x > 0; x--) { console.log('C is fun'); }
}
