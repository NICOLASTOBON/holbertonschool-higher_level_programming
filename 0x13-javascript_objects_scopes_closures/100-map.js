#!/usr/bin/node
const array = require('./100-data').list;

const value = array.map(item => item * array.indexOf(item));
console.log(array);
console.log(value);
