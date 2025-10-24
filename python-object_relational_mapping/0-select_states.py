#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    
    # Execute query to get all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch and print all results
    for state in cursor.fetchall():
        print(state)

    # Close connection
    cursor.close()
    db.close()
