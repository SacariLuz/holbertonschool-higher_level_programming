#!/usr/bin/python3
"""Listado de todos los estados con N"""

from sys import argv
import MySQLdb

def main():
    """
    """

    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               password=password,
                               db=dbname)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name \ LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))
    cur.close()
    database.close()

if __name__ == "__main__":
    main()
