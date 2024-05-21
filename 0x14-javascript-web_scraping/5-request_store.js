#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.error('error:', err); // Print the error if one occurred during writing the file
      }
    });
  }
});
