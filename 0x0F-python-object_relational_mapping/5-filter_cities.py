#!/usr/bin/python3

"""
module 5-cities_by_state
lists all cities in db
"""


import MySQLdb
import sys


def filter_state(username, password, database_name, state_name):
    """
    displays all cities in a state
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    cur = db.cursor()

    query = "SELECT DISTINCT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s \
    ORDER BY (SELECT cities.id FROM cities WHERE \
    cities.name = cities.name LIMIT 1)"

    cur.execute(query, (state_name,))

    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database_name, state_name = sys.argv[1], \
     sys.argv[2], sys.argv[3], sys.argv[4]

    filter_state(username, password, database_name, state_name)
