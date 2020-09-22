#!/usr/bin/node
const request = require('request');
const args = process.argv;
const URL = 'https://swapi-api.hbtn.io/api/films/:id';

request(`${URL.replace(':id', args[2])}`, (err, response, body) => {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(err);
  }
});
