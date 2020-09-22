#!/usr/bin/node
const fs = require('fs');
const argvs = process.argv;

fs.writeFile(argvs[2], argvs[3], 'utf-8', (err) => {
  if (err) {
      console.log(err);
  }
});
