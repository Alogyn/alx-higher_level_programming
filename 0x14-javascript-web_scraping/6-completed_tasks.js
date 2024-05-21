#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });

  console.log(completedTasks);
});
