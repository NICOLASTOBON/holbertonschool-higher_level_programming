#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(args[2], (err, response) => {
  if (err) throw console.log(err);
  console.log('code: ', response.statusCode);
});
