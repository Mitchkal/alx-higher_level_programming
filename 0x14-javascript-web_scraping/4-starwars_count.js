#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
let count = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const result = data.results;
    for (let i = 0; i < result.length; i++) {
      if (result[i].characters) {
        for (const k of result[i].characters) {
          if (k.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
