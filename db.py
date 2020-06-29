import sqlite3


class Database:     
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        # db tables
        self.roles = 'roles'
        self.statuses = 'statuses'
        self.tasks = 'tasks'
        self.users = 'users'

  
    def get_users(self, role = 1):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.users}` WHERE `role` = ?", (role,)).fetchall()

 
    # Is user exists
    def user_exists(self, user_id, role = 1):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.users}` WHERE `id` = ? AND `role` = ?", (user_id, role)).fetchall()


    # Add task
    def add_task(self, task, user_id):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `{self.tasks}` (`task`, `customer`) VALUES (?,?)", (task, user_id)), self.cursor.lastrowid

    
    # Update status
    def update_status(self, task_id, status_id):
        with self.connection:
            return self.cursor.execute(f"UPDATE `{self.tasks}` SET `status` = ? WHERE `id` = ?", (status_id, task_id))


    # Get statuses
    def get_statuses(self, except_status):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}` WHERE `id` != ?", (except_status,)).fetchall()


    def get_tasks(self, status = 1):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}` WHERE `status` == ? ORDER BY `id` DESC", (status,)).fetchall()

    
    def get_task(self, task_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}` WHERE `id` == ?", (task_id,)).fetchall()
    
    
    def get_tasks_except_completed(self):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}` WHERE `status` != ?", (3,)).fetchall()

    
    def get_status(self, status_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}` WHERE `id` == ?", (status_id,)).fetchall()

    
    def get_status_name(self, status_id):
        with self.connection:
            return self.cursor.execute(f"SELECT `status` FROM `{self.statuses}` WHERE `id` = ?", (status_id,)).fetchall()


    def get_status_by_name(self, name):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}` WHERE `status` = ?", (name,)).fetchall()


    def task_exists(self, task_id):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}` WHERE `id` = ?", (task_id,)).fetchall()


    def status_exists_by_name(self, name):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}` WHERE `status` = ?", (name,)).fetchall()


    # Close connection with db
    def close(self):
        self.connection.close()