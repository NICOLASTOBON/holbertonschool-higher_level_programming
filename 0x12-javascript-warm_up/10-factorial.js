#!/usr/bin/node

const value = Number(process.argv[2]);

if (isNaN(value)) {
  console.log(1);
} else {
  console.log(factorial(value));
}

function factorial (num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
