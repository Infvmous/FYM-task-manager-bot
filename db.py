import sqlite3


class Db:   
    
    
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()


    # Is customer exists
    def customer_exists(self, customer_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `customers` WHERE `id` = ?", (customer_id,)).fetchall()


    # Create task
    def create_task(self, task, customer_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `tasks` (`task`, `customer`) VALUES (?,?)", (task, customer_id))

    
    # Update status
    def update_status(self, task_id, status_id):
        with self.connection:
            return self.cursor.execute("UPDATE `tasks` SET `status` = ? WHERE `id` = ?", (status_id, task_id))

    
    # Close connection with db
    def close(self):
        self.connection.close()