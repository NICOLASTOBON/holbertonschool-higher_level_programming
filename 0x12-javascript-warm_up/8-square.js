#!/usr/bin/node

const value = Number(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    let v = '';
    for (let j = 0; j < value; j++) {
      v += 'X';
    }
    console.log(v);
  }
}
