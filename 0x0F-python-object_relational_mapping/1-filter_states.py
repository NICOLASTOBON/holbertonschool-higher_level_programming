#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)"""

import MySQLdb as _mysql
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]

    my_db = _mysql.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=name_db,
        charset="utf8"
    )

    cur = my_db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC;")
    for state in cur.fetchall():
        print(state)
    cur.close
    my_db.close
