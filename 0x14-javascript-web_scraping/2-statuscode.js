#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    console.log(`code: ${response.statusCode}`); // Print the response status code if a response was received
  }
});
