import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to the database successfully")

# # Create tables in the appropriate order

# # Department table
# conn.execute('CREATE TABLE department_new (department_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
# print("Created department table new successfully!")

# # Status table
# conn.execute('''CREATE TABLE status_new (
#                     status_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created status table new successfully!")

# # Admin table
# conn.execute('''CREATE TABLE admin_new (
#                     admin_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT, 
#                     email TEXT
#                 )''')
# print("Created admin table new successfully!")

# # Role table
# conn.execute('''CREATE TABLE role_new (
#                     role_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     role_name TEXT, 
#                     description TEXT
#                 )''')
# print("Created role table new successfully!")

# # Personnel table
# conn.execute('''CREATE TABLE personnel_new (
#                     personnel_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     role_id INTEGER, 
#                     name TEXT, 
#                     email TEXT, 
#                     FOREIGN KEY(role_id) REFERENCES role_new(role_id)
#                 )''')
# print("Created personnel table new successfully!")

# # Event table
# conn.execute('''CREATE TABLE event_new (
#                     event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     event_name TEXT, 
#                     status_id INTEGER, 
#                     FOREIGN KEY(status_id) REFERENCES status_new(status_id)
#                 )''')
# print("Created event table new successfully!")

# # Project_event table
# conn.execute('''CREATE TABLE project_event_new (
#                     project_event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     project_id INTEGER, 
#                     event_id INTEGER, 
#                     date TEXT, 
#                     status_id INTEGER, 
#                     FOREIGN KEY(status_id) REFERENCES status_new(status_id)
#                 )''')
# print("Created project_event table new successfully!")

# # Event_personnel table
# conn.execute('''CREATE TABLE event_personnel_new1 (
#                     personnel_id INTEGER, 
#                     project_event_id INTEGER, 
#                     PRIMARY KEY (personnel_id, project_event_id),
#                     FOREIGN KEY(personnel_id) REFERENCES personnel_new(personnel_id), 
#                     FOREIGN KEY(project_event_id) REFERENCES project_event_new1(project_event_id)
#                 )''')
# print("Created event_personnel_new1 table successfully!")

# # Mandatory table
# conn.execute('''CREATE TABLE mandatory_new (
#                     mandatory_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created mandatory table new successfully!")

# # Project_mandatory table
# conn.execute('''CREATE TABLE project_mandatory_new1 (
#                     mandatory_id INTEGER, 
#                     project_id INTEGER, 
#                     PRIMARY KEY (mandatory_id, project_id),
#                     FOREIGN KEY(mandatory_id) REFERENCES mandatory_new(mandatory_id),
#                     FOREIGN KEY(project_id) REFERENCES project_info_new1(project_id)
#                 )''')
# print("Created project_mandatory_new1 table successfully!")

# # Recipient table
# conn.execute('''CREATE TABLE recipient_new (
#                     recipient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                     name TEXT
#                 )''')
# print("Created recipient table new successfully!")

# # Project_recipient table
# conn.execute('''CREATE TABLE project_recipient_new1 (
#                     recipient_id INTEGER, 
#                     project_id INTEGER, 
#                     PRIMARY KEY (recipient_id, project_id),
#                     FOREIGN KEY(recipient_id) REFERENCES recipient_new(recipient_id),
#                     FOREIGN KEY(project_id) REFERENCES project_info_new1(project_id)
#                 )''')
# print("Created project_recipient_new1 table successfully!")

# Requester table
conn.execute('''CREATE TABLE requester_new (
                    requester_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    email TEXT, 
                    contact TEXT, 
                    department_id INTEGER, 
                    FOREIGN KEY(department_id) REFERENCES department_new(department_id)
                )''')
print("Created requester table new successfully!")

# Project_info table
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

# Commit changes and close the connection
conn.commit()
conn.close()
