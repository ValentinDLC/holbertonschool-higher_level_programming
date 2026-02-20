#!/usr/bin/python3
"""List states matching argument safely to prevent SQL injection"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    
    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC;", (sys.argv[4],))
    
    for state in cursor.fetchall():
        print(state)
    
    cursor.close()
    db.close()
