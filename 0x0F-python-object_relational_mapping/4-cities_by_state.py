#!/usr/bin/python3

"""
module 4-cities_by_state
lists all cities in db
"""


import MySQLdb
import sys


def filter_state(username, password, database_name):
    """
    displays all cities
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM \
    cities JOIN states ON cities.state_id = states.id ORDER BY cities.id"

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], \
     sys.argv[2], sys.argv[3]

    filter_state(username, password, database_name)
