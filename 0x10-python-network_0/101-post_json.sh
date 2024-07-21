#!/bin/bash
# sends a JSON POST req
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
