#!/bin/bash
#  that sends a request to a URL
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
