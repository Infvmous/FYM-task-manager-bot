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
    
    
    def get(self, table, value, column = '*', row = 'id'):
        with self.conn:
            query = "SELECT {0} FROM {1}\
                    WHERE {2} = ?".format(column, table, row)
            return self.cur.execute(query, (value,)).fetchone()


    def update(self, table, value1, row1, value2, row2 = 'id'):
        with self.conn:
            query = "UPDATE {0}\
                    SET {1} = ?\
                    WHERE {2} = ?".format(table, row1, row2)
            return self.cur.execute(query, (value1, value2))
    

    def add_task(self, name, user_id, date, task_type = 6):
        with self.conn:
            query = f"INSERT INTO `tasks`\
                    (`name`, `customer`, `type`, `date`)\
                    VALUES (?,?,?,?)"
            return self.cur.execute(query, (name, user_id, task_type, date)), self.cur.lastrowid
    

    def get_users(self, group = 1):
        with self.conn:
            query = "SELECT * FROM `users`\
                    WHERE `group` = ?"
            return self.cur.execute(query, (group,)).fetchall()
    

    def get_task_statuses(self, except_status):
        with self.conn:
            query = "SELECT * FROM `task_statuses`\
                    WHERE `id` != ?"
            return self.cur.execute(query, (except_status,)).fetchall()

    



