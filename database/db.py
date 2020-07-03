import sqlite3
import logging


class Database:
    def __init__(self, name = None):
        self.conn = None
        self.cur = None
        if name: self.open(name)


    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cur = self.conn.cursor()
            logging.info('DATABASE - connected successfully')
        except sqlite3.Error as e:
            logging.info('DATABASE - ERROR - not connected')
    

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    

    def get_all(self, table):
        with self.conn:
            query = "SELECT * FROM {0}".format(table)
            return self.cur.execute(query).fetchall()
    
    
    def get_where(self, table, value, row = 'id'):
        with self.conn:
            query = "SELECT * FROM {0}\
                    WHERE {1} = ?".format(table, row)
            return self.cur.execute(query, (value,)).fetchone()
    

    



