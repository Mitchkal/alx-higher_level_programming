#!/usr/bin/python3
"""
module 0-select_stats
parameters: username, password, dbname
"""


import MySQLdb
import sys


def list_states(username, password, database_name):
    """
    lists states from database
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, database_name)
