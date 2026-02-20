#!/usr/bin/python3
"""Print all cities of a given state (filter by state name)
Safe from SQL injection and uses only one execute() call.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Parameterized query to avoid SQL injection (single execute)
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC;")
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    # If any results, join city names with comma and space
    if rows:
        city_names = ", ".join(row[0] for row in rows)
        print(city_names)

    cursor.close()
    db.close()
