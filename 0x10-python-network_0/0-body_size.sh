#!/bin/bash
# displays the size of a response
curl -s "$1" | wc -c
