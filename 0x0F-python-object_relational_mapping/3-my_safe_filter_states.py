#!/usr/bin/python3

import sys
import MySQLdb

"""
module safe filter state
Searches for state in db
safe from SQL injection
"""


def filter_state(username, password, database_name, state_name):
    """
    displays searched state
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY\
    states.id"

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name, state_name = sys.argv[1], \
     sys.argv[2], sys.argv[3], sys.argv[4]

    filter_state(username, password, database_name, state_name)
