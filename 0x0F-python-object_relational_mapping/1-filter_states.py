#!/usr/bin/python3
"""
connects to db and lists all states
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """simple doc for testing"""
    db = MySQLdb.connect(
            host=127.0.0.1, port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'
            ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
