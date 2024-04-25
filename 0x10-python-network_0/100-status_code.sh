#!/bin/bash
# Script to display only the status code of the response from a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
