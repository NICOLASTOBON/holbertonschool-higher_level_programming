#!/usr/bin/node
const value = process.argv;

function add (a, b) {
  return (a + b);
}
console.log(add(Number(value[2]), Number(value[3])));
