#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const getTasksByUserId = async () => {
  request(apiUrl, { json: true }, async (error, response, todos) => {
    if (error) {
      console.error(error);
      return;
    }
    const completedTasksByUserId = {};

    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUserId[userId] = (completedTasksByUserId[userId] || 0) + 1;
      }
    }
    console.log(completedTasksByUserId);
  });
};
getTasksByUserId();
