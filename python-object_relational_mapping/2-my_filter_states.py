#!/usr/bin/python3
""" scrip que filtra los valores en la tabla de estados de hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    sname = argv[4]

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               password=password,
                               db=dbname)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name \
        LIKE BINARY '{}' ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))
    cur.close()
    database.close()
