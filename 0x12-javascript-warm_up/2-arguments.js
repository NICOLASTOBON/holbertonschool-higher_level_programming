#!/usr/bin/node

const value = process.argv.length;

if (value < 3) {
  console.log('No argument');
} else if (value === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
