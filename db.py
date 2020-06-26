import sqlite3


class Db:
    
    
    def __init__(self, db_file):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    # Is user a customer
    def is_customer(self, id):
        with self.connection:
            pass
    

    # Create task
    def create_task(self, task, customer_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `tasks` (`task`, `customer`) VALUES (?,?)", (task, customer_id))

    
    # Update status
    def update_status(self, task_id, status_id):
        with self.connection:
            return self.cursor.execute("UPDATE `tasks` SET `status` = ? WHERE `id` = ?", (status_id, task_id))