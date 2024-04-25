#!/bin/bash
# Script to send a request that triggers a specific response from the server
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
