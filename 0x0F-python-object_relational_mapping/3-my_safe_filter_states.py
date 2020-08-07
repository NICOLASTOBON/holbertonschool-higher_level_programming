#!/usr/bin/python3
# write one that is safe from MySQL injections!

import MySQLdb as _mysql
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]
    state_name = sys.argv[4]

    my_db = _mysql.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=name_db,
        charset="utf8"
    )

    cur = my_db.cursor()
    txt_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC;"
    cur.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC;", (state_name,)
        )

    for state in cur.fetchall():
        print(state)

    cur.close
    my_db.close
