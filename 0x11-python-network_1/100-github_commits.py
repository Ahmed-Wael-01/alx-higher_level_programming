#!/usr/bin/python3
"""
lists last ten commits
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    coms = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                    coms[i].get("sha"),
                    coms[i].get("commit").get("author").get("name")))
    except Exception as e:
        pass
