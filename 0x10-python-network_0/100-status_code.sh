#!/bin/bash
#  that sends a request to a URL
curl -sI "$1" -o /dev/null -w '%{http_code}'
