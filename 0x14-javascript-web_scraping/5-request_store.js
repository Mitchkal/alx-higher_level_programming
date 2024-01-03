#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  fs.writeFile(filepath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error(writeError);
    }
  });
});
