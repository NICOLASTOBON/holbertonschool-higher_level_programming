#!/usr/bin/node
const array = require('./100-data').list;

const value = array.map((item, index) => item * index);
console.log(array);
console.log(value);
