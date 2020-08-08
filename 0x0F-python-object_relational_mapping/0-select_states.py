#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]

    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=name_db,
        charset="utf8"
        )
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    list_all = cur.fetchall()
    for row in list_all:
        print(row)
    cur.close
    my_db.close
