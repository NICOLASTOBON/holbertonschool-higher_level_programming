#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const size = this.height;

    for (let i = 0; i < size; i++) {
      let val = '';
      for (let j = 0; j < size; j++) {
        val += c;
      }
      console.log(val);
    }
  }
}

module.exports = Square;
