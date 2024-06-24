#!/usr/bin/python
"""
connects to db and lists all states
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host=127.0.0.1, port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
