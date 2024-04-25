#!/bin/bash
# Script to display all HTTP methods a server will accept for a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
