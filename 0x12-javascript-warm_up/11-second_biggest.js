#!/usr/bin/node

const value = process.argv;

if (value.length <= 3) {
  console.log(0);
} else {
  const newArr = value.slice(2).sort((a, b) => a - b);
  console.log(newArr[newArr.length - 2]);
}
