#!/usr/bin/python3

"""
module 1-filter_states
filters states starting with n
"""


import sys
import MySQLdb


def filter_states(username, password, database_name):
    """
    filters states starting with a
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, database_name)
