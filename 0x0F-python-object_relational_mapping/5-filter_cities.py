#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

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
    cur.execute("""SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name=%s ORDER BY cities.id ASC;""", (state_name,))

    res = cur.fetchall()
    print(", ".join(i[0] for i in res))
    cur.close
    my_db.close
