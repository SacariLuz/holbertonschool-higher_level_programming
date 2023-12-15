#!/usr/bin/python3
"""
Script que toma el nombre de un estado como argumento y lista las ciudades de ese estado.
Usando la database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM cities AS cities \
            INNER JOIN states AS states \
            ON cities.state_id = states.id \
            ORDER BY cities.id")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
