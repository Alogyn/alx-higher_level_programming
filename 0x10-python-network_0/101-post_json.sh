#!/bin/bash
# Script to send a JSON POST request from a file and display the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
