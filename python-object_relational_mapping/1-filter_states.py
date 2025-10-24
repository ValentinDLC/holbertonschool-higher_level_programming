#!/usr/bin/python3
"""List states starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    
    # Execute query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    
    # Fetch and print results
    for state in cursor.fetchall():
        print(state)
    
    cursor.close()
    db.close()
