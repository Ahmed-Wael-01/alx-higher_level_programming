#!/bin/bash
# view acceptable methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
