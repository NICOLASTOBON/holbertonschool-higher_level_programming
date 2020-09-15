#!/usr/bin/node

const value = process.argv[2];
const isNum = isNaN(Number(value));

console.log(isNum ? 'Not a number' : `My number: ${Number(value)}`);
