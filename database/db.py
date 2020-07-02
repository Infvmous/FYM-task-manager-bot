import sqlite3


class Database:     
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.roles = 'roles'
        self.statuses = 'statuses'
        self.tasks = 'tasks'
        self.users = 'users'

  
    def get_users(self, role = 1):
        """ Get all users with role from database

        Args:
            role (int): User role. Defaults to 1.

        Returns:
            list: users list
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.users}`\
                                        WHERE `role` = ?", (role,)).fetchall()

 
    def add_user(self, user_id, username, full_name, role):
        """ Add user to database

        Args:
            user_id (int): user id
            username (varchar): telegram username
            full_name (varchar): full name
            role (int): role id

        Returns:
            list: list of inserted args
        """
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `{self.users}`\
                                        (`id`, `username`, `full_name`, `role`)\
                                        VALUES (?,?,?,?)", (user_id, username, full_name, role))
    

    def user_exists(self, user_id, role = 1):
        """ Is user exists or not in database

        Args:
            user_id (int): user id
            role (int): role id. Defaults to 1.

        Returns:
            list: user data
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.users}`\
                                        WHERE `id` = ? AND `role` = ?", (user_id, role)).fetchall()


    def add_task(self, task, user_id):
        """ Add new task to database

        Args:
            task (text): task description
            user_id (int): user id

        Returns:
            list: list of inserted args
        """
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `{self.tasks}`\
                                        (`task`, `customer`)\
                                        VALUES (?,?)", (task, user_id)), self.cursor.lastrowid

    
    def update_status(self, task_id, status_id):
        """ Update status for specific task

        Args:
            task_id (int): task id
            status_id (int): status id

        Returns:
            bool: True or False depends on query success of executing
        """
        with self.connection:
            return self.cursor.execute(f"UPDATE `{self.tasks}`\
                                        SET `status` = ?\
                                        WHERE `id` = ?", (status_id, task_id))



    def get_statuses(self, except_status):
        """ Get all statuses except only one

        Args:
            except_status (int): status id

        Returns:
            list: list of received statuses
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}`\
                                        WHERE `id` != ?", (except_status,)).fetchall()


    def get_tasks(self, status = 1):
        """ Get all tasks with specific status

        Args:
            status (int): status id. Defaults to 1.

        Returns:
            list: list of received tasks
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}`\
                                        WHERE `status` == ?\
                                        ORDER BY `id` DESC", (status,)).fetchall()

    
    def get_task(self, task_id):
        """ Get specific task by id

        Args:
            task_id (int): task id

        Returns:
            list: list of received tasks
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}`\
                                        WHERE `id` == ?", (task_id,)).fetchall()
    
    
    def get_tasks_except_completed(self):
        """ Get all tasks except completed

        Returns:
            list: list of received tasks
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}`\
                                        WHERE `status` != ?", (3,)).fetchall()

    
    def get_status(self, status_id):
        """ Get specific status by id

        Args:
            status_id (int): status id

        Returns:
            list: status data
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}`\
                                        WHERE `id` == ?", (status_id,)).fetchall()

    
    def get_status_name(self, status_id):
        """ Get status name by id

        Args:
            status_id (id): status id

        Returns:
            list: status name inside list
        """
        with self.connection:
            return self.cursor.execute(f"SELECT `status` FROM `{self.statuses}`\
                                        WHERE `id` = ?", (status_id,)).fetchall()


    def get_status_by_name(self, name):
        """ Get status by name

        Args:
            name (varchar): status name

        Returns:
            list: status data
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.statuses}`\
                                        WHERE `status` = ?", (name,)).fetchall()


    def task_exists(self, task_id):
        """ Is task exists inside database

        Args:
            task_id (int): task id

        Returns:
            list: task data
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.tasks}`\
                                        WHERE `id` = ?", (task_id,)).fetchall()


    def get_roles(self):
        """ Get all roles from database

        Returns:
            list: list of received roles
        """
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM `{self.roles}`").fetchall()

    
    def get_role(self, role_id):
        """ Get specific role from database

        Args:
            role_id (int): role id

        Returns:
            list: role data
        """
        with self.connection:
            return str(self.cursor.execute(f"SELECT `role` FROM `{self.roles}`\
                                            WHERE `id` = ?", (role_id,)).fetchall())


    def close(self):
        """ Close database connection """
        self.connection.close()