#!/usr/bin/node
const newDict = require('./101-data').dict;

const data = {};

for (const [key, value] of Object.entries(newDict)) {
  if (data[value]) {
    data[value].push(key);
  } else {
    data[value] = [key];
  }
}
console.log(data);
