#!/bin/bash
# Script to fetch the body of a URL response only if the status code is 200

curl -sL "$1"
