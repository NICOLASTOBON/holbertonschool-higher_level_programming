#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(args[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
