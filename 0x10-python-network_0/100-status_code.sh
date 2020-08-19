#!/bin/bash
#  that sends a request to a URL
curl -sI "$1" | grep HTTP | cut -d ' ' -f2
