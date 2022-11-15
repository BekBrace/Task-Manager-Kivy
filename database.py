import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('todo.db')
        self.cursor = self.con.cursor()
        self.create_task_table()

    '''CREATE the Tasks TABLE'''
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task varcahr(50) NOT NULL, due_date varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)))")
    
    '''CREATE A Task'''
    def create_task(self, task, due_date=None):
        self.cursor.execute("INSERT INTO tasks(task, due_date, completed) VALUES(?, ?, ?)", (task, due_date, 0))
        self.con.commit()

        # Getting the last entered item to add in the list
        created_task = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE task = ? and completed = 0", (task,)).fetchall()
        return created_task[-1]
    
    '''READ / GET the tasks'''
    def get_tasks(self):
        
        # Getting all complete and incomplete tasks
        
        complete_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        incomplete_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 0").fetchall()

        return incomplete_tasks , complete_tasks


    '''UPDATING the tasks status'''
    def mark_task_as_complete(self, taskid):
        self.cursor.execute("UPDATE tasks SET completed=1 WHERE id=?",(taskid,))
        self.con.commit()

    def mark_task_as_incomplete(self, taskid):
        self.cursor.execute("UPDATE tasks SET completed=0 WHERE id=?",(taskid,))
        self.con.commit()
        
        # returning the task text
        task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (taskid,)).fetchall()
        return task_text[0][0]

    '''Deleting the task'''
    def delete_task(self, taskid):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (taskid,))
        self.con.commit()
    '''Closing the connection '''
    def close_db_connection(self):
        self.con.close()