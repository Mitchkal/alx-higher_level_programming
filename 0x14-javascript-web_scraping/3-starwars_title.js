#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    if (data.detail) {
      console.error('Error: ' + data.detail);
    } else {
      console.log(data.title);
    }
  }
});
