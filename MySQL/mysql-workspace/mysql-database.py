import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
        host='localhost',
        user='root',
        password='mysqlpass',
        database=db_name
        )
    
    except Exception as e:
        print(e)

def add_new_project(cursor, project_title, project_description, task_description):
    
    project_data = (project_title, project_description)
    cursor.execute("""INSERT INTO projects(title, description) 
                      VALUES (%s,%s)""", project_data)
    
    project_id = cursor.lastrowid
    task_data = []
    
    for description in task_description:
        task_data.append((project_id, description))

    cursor.executemany('''INSERT INTO tasks(project_id, description)
                          VALUES (%s,%s)''', task_data)

if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()
    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_new_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    task_records = cursor.fetchall()
    print(task_records)
    db.close()