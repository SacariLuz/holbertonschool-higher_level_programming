#!/usr/bin/python3
"""
Script que liste todas las ciudades de la database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities AS cities \
            INNER JOIN states AS states \
            ON cities.state_id = states.id \
            ORDER BY cities.id")
    [print(city) for city in cur.fetchall()]
