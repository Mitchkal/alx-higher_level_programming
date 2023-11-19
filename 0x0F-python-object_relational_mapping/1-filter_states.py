#!/usr/bin/python3

import MySQLdb
import sys
"""
module 1-filter_states
filters staes starting with n
"""


def filter_states(username, password, database_name):
    """
    filters states starting with N
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, database_name)
