#!/usr/bin/node

exports.logMe = (function () {
  let count = 0;

  return (item) => {
    console.log(`${count}: ${item}`);
    count++;
  };
}());
