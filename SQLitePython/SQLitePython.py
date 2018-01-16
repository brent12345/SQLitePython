import sqlite3
from sqlite3 import Error
import re

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM albums")
 
    rows = cur.fetchall()
 
    #for row in rows:
        #matchObj = re.match('(?<=-)\w+', row[1])
        #if matchObj in row:
            #print(row) 
        #else:
        #    continue   
    return rows
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    with conn:
        rows = select_all_tasks(conn)
        return rows
    


 




