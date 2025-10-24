#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa
Comments in English in a studious tone.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Single execute() as required: join cities and states and order by cities.id
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC;")
    cursor.execute(query)

    # Print each row exactly as in example: tuple-like printed representation
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
