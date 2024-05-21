#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title); // Print the title of the movie
  } else {
    console.log(`Error: ${response.statusCode}`); // Handle non-200 status codes
  }
});
