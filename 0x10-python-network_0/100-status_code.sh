#!/bin/bash
#status code
curl -o log-data -sw "%{http_code}" "$1"
