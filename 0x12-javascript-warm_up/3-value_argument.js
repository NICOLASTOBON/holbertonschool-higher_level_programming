#!/usr/bin/node

const value = process.argv.length;

if (value < 3) {
  console.log('No argument');
} else {
  for (let i = 2; i < value; i++) {
    console.log(process.argv[i]);
  }
}
