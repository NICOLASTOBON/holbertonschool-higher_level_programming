#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const width = this.width;
    const height = this.height;

    for (let i = 0; i < height; i++) {
      let val = '';
      for (let j = 0; j < width; j++) {
        val += 'X';
      }
      console.log(val);
    }
  }
}

module.exports = Rectangle;
