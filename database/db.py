import sqlite3
import logging


class Database:
    def __init__(self, name = None):
        self.conn = None
        self.cur = None
        if name: self.open(name)
        self.accs = 'accounts'
        self.groups = 'groups'
        self.stats = 'statuses'
        self.tasks = 'tasks'
        self.types = 'types'
        self.users = 'users'


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
    

    def get_user(self, user_id):
        with self.conn:
            query = f"SELECT * FROM {self.users}\
                    WHERE `external_id` = ?"
            return self.cur.execute(query, (user_id,)).fetchone()



