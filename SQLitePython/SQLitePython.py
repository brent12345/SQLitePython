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
 
    for row in rows:
        matchObj = re.match(r'(.*)Sa(.*?) .*', row[1])
        if matchObj in row:
            print(row) 
        else:
            continue   
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    with conn:
        select_all_tasks(conn)
    


 
if __name__ == '__main__':
    create_connection("chinook.db")



