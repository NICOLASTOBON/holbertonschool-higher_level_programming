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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

class Square extends Rectangle {
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
