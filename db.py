import sqlite3


class Db:   
    
    
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

  
    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `customer` = ? AND `admin` = ?", (False, False)).fetchall()


    def get_customers(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `customer` = ?", (True,)).fetchall()
    

    def get_admins(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user` WHERE `admin` = ?", (True,)).fetchall()

    
    # Is user exists in db
    def user_is_customer(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `id` = ? AND `customer` = ?", (user_id, True)).fetchall()


    # Add user to db
    def add_user(self, user_id, username, customer = False):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`id`, `username`, `customer`) VALUES (?,?,?)", (user_id, username, customer))

    
    # Add task
    def add_task(self, task, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `tasks` (`task`, `customer`) VALUES (?,?)", (task, user_id))

    
    # Update status
    def update_status(self, task_id, status_id):
        with self.connection:
            return self.cursor.execute("UPDATE `tasks` SET `status` = ? WHERE `id` = ?", (status_id, task_id))


    # Get statuses
    def get_statuses(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `statuses`").fetchall()

    
    # Close connection with db
    def close(self):
        self.connection.close()