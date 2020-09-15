#!/usr/bin/node

const value = Number(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
