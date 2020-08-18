#!/bin/bash
# script that takes in a URL, sends a POST request
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
