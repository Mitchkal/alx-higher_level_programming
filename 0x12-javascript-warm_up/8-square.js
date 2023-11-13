#!/usr/bin/node
const [, , argv1] = process.argv;

const size = parseInt(argv1);

let height = 0;
let width = 0;
let output = '';
if (isNaN(size)) {
	console.log('Missing size');
} else {
  for (height = 0; height < size; height++) {
    for (width = 0; width < size; width++) {
      output += 'x';
    }
    console.log(output);
    output = '';
  }
}
