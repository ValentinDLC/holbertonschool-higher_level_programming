#!/usr/bin/python3
"""List states that match the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    
    # Build query using format (unsafe version)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(sys.argv[4])
    cursor.execute(query)
    
    for state in cursor.fetchall():
        print(state)
    
    cursor.close()
    db.close()
