#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('error:', error); // Print the error if one occurred
        return;
      }

      if (response.statusCode !== 200) {
        console.log(`Error: ${response.statusCode}`); // Handle non-200 status codes
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
