#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
            SELECT
                cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
