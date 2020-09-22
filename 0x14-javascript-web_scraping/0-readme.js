#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString('utf-8'));
  }
});
