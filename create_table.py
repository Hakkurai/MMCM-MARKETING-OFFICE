import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# # department table
# conn.execute('CREATE TABLE department_new (department_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
# print("Created department table new successfully!")

# # requester table
# conn.execute('''CREATE TABLE requester_new (
#                     requester_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT, 
#                     email TEXT, 
#                     contact TEXT, 
#                     department_id INTEGER, 
#                     FOREIGN KEY(department_id) REFERENCES department(department_id)
#                 )''')
# print("Created requester table new successfully!")

# # project_event 
# conn.execute('''CREATE TABLE project_event_new (
#                     project_event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     project_id INTEGER, 
#                     event_id INTEGER, 
#                     date TEXT, 
#                     status_id INTEGER, 
#                     FOREIGN KEY(status_id) REFERENCES status(status_id)
#                 )''')
# print("Created project_event table new successfully!")

# # status table
# conn.execute('''CREATE TABLE status_new (
#                     status_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created status table new successfully!")

# # event table
# conn.execute('''CREATE TABLE event_new (
#                     event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     event_name TEXT, 
#                     status_id INTEGER, 
#                     FOREIGN KEY(status_id) REFERENCES status(status_id)
#                 )''')
# print("Created event table new successfully!")

# # admin table
# conn.execute('''CREATE TABLE admin_new (
#                     admin_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT, 
#                     email TEXT
#                 )''')
# print("Created admin table new successfully!")


# # event personnel table
# conn.execute('''CREATE TABLE event_personnel_new1 (
#                     personnel_id INTEGER, 
#                     project_event_id INTEGER, 
#                     PRIMARY KEY (personnel_id, project_event_id),
#                     FOREIGN KEY(personnel_id) REFERENCES personnel(personnel_id), 
#                     FOREIGN KEY(project_event_id) REFERENCES project_event(project_event_id)
#                 )''')
# print("Created event_personnel_new1 table successfully!")

# # role table
# conn.execute('''CREATE TABLE role_new (
#                     role_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     role_name TEXT, 
#                     description TEXT
#                 )''')
# print("Created role table new successfully!")

# # personnel table
# conn.execute('''CREATE TABLE personnel_new (
#                     personnel_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     role_id INTEGER, 
#                     name TEXT, 
#                     email TEXT, 
#                     FOREIGN KEY(role_id) REFERENCES role(role_id)
#                 )''')
# print("Created personnel table new successfully!")

# # mandatory table
# conn.execute('''CREATE TABLE mandatory_new (
#                     mandatory_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created mandatory table new successfully!")

# # project_mandatory table
# conn.execute('''CREATE TABLE project_mandatory_new1 (
#                     mandatory_id INTEGER, 
#                     project_id INTEGER, 
#                     PRIMARY KEY (mandatory_id, project_id),
#                     FOREIGN KEY(mandatory_id) REFERENCES mandatory(mandatory_id),
#                     FOREIGN KEY(project_id) REFERENCES project_info(project_id)
#                 )''')
# print("Created project_mandatory_new1 table successfully!")


# # recipient table
# conn.execute('''CREATE TABLE recipient_new (
#                     recipient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created recipient table new successfully!")


# # project_recipient table
# conn.execute('''CREATE TABLE project_recipient_new1 (
#                     recipient_id INTEGER, 
#                     project_id INTEGER, 
#                     PRIMARY KEY (recipient_id, project_id),
#                     FOREIGN KEY(recipient_id) REFERENCES recipient(recipient_id),
#                     FOREIGN KEY(project_id) REFERENCES project_info(project_id)
#                 )''')
# print("Created project_recipient_new1 table successfully!")


# project_info table
conn.execute('''CREATE TABLE project_info_new1 (
                    project_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    requester_id INTEGER, 
                    project_title TEXT,
                    output TEXT, 
                    objective TEXT, 
                    recipient TEXT,
                    mandatory TEXT,
                    date_filed TEXT, 
                    date_needed TEXT, 
                    add_info TEXT, 
                    admin_id INTEGER, 
                    status_id INTEGER, 
                    FOREIGN KEY(requester_id) REFERENCES requester_new(requester_id), 
                    FOREIGN KEY(admin_id) REFERENCES admin_new(admin_id), 
                    FOREIGN KEY(status_id) REFERENCES status_new(status_id)
                )''')
print("Created project_info table new successfully!")

conn.close()