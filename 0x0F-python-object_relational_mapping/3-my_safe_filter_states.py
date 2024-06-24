#!/usr/bin/python3
"""
connects to db and lists all states ddhdfjhds
asjkbkjdbf adfbjkadfbkj adbfjbdfjbdf
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host=127.0.0.1, port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
