#!/usr/bin/python3
"""
    python script to fetch alx website
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        con = res.read()
        print("""
Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(
                            type(con),
                            con,
                            con.decode('utf-8')))
