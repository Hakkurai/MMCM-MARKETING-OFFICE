import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# department table
conn.execute('CREATE TABLE department (department_id INTEGER PRIMARY KEY, name TEXT)')
print("Created department table successfully!")

# requester table
conn.execute('''CREATE TABLE requester (
                    requester_id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    email TEXT, 
                    contact TEXT, 
                    department_id INTEGER, 
                    FOREIGN KEY(department_id) REFERENCES department(department_id)
                )''')
print("Created requester table successfully!")

# project_event
conn.execute('''CREATE TABLE project_event (
                    project_event_id INTEGER PRIMARY KEY, 
                    project_id INTEGER, 
                    event_id INTEGER, 
                    date TEXT, 
                    status_id INTEGER, 
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )''')
print("Created project_event table successfully!")

# status table
conn.execute('''CREATE TABLE status (
                    status_id INTEGER PRIMARY KEY, 
                    name TEXT
                )''')
print("Created status table successfully!")

# event table
conn.execute('''CREATE TABLE event (
                    event_id INTEGER PRIMARY KEY, 
                    event_name TEXT, 
                    status_id INTEGER, 
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )''')
print("Created event table successfully!")

# admin table
conn.execute('''CREATE TABLE admin (
                    admin_id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    email TEXT
                )''')
print("Created admin table successfully!")

# event personnel table
conn.execute('''CREATE TABLE event_personnel_new (
                    personnel_id INTEGER, 
                    project_event_id INTEGER, 
                    status_id INTEGER, 
                    PRIMARY KEY (personnel_id, project_event_id, status_id),
                    FOREIGN KEY(project_event_id) REFERENCES project_event(project_event_id), 
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )''')
print("Created event_personnel_new table successfully!")

# role table
conn.execute('''CREATE TABLE role (
                    role_id INTEGER PRIMARY KEY, 
                    role_name TEXT, 
                    description TEXT
                )''')
print("Created role table successfully!")

# personnel table
conn.execute('''CREATE TABLE personnel (
                    personnel_id INTEGER PRIMARY KEY, 
                    role_id INTEGER, 
                    name TEXT, 
                    email TEXT, 
                    FOREIGN KEY(role_id) REFERENCES role(role_id)
                )''')
print("Created personnel table successfully!")

# mandatory table
conn.execute('''CREATE TABLE mandatory (
                    mandatory_id INTEGER PRIMARY KEY, 
                    name TEXT
                )''')
print("Created mandatory table successfully!")

# project_mandatory table
conn.execute('''CREATE TABLE project_mandatory_new (
                    mandatory_id INTEGER, 
                    project_id INTEGER, 
                    PRIMARY KEY (mandatory_id, project_id),
                    FOREIGN KEY(mandatory_id) REFERENCES mandatory(mandatory_id)
                )''')
print("Created project_mandatory table successfully!")

# recipient table
conn.execute('''CREATE TABLE recipient (
                    recipient_id INTEGER PRIMARY KEY, 
                    name TEXT
                )''')
print("Created recipient table successfully!")

# project_recipient table
conn.execute('''CREATE TABLE project_recipient_new (
                    recipient_id INTEGER, 
                    project_id INTEGER, 
                    PRIMARY KEY (recipient_id, project_id),
                    FOREIGN KEY(recipient_id) REFERENCES recipient(recipient_id)
                )''')
print("Created project_recipient_new table successfully!")

# project_info table
conn.execute('''CREATE TABLE project_info (
                    project_id INTEGER PRIMARY KEY, 
                    requester_id INTEGER, 
                    output TEXT, 
                    objective TEXT, 
                    date_filed TEXT, 
                    date_needed TEXT, 
                    add_info TEXT, 
                    admin_id INTEGER, 
                    status_id INTEGER, 
                    FOREIGN KEY(requester_id) REFERENCES requester(requester_id), 
                    FOREIGN KEY(admin_id) REFERENCES admin(admin_id), 
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )''')
print("Created project_info table successfully!")

conn.close()