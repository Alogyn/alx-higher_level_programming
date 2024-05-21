#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });

  console.log(count);
});
