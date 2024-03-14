import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return render_template("login.html")

# Define the login route
@app.route("/login", methods=["POST"])
def login():
    role = request.form.get("role")
    if role == "student":
        return redirect(url_for("requester_form"))
    elif role == "admin":
        return redirect(url_for("admin_login"))
    else:
        return "Invalid role"

# Define the requester_form route
@app.route("/requester_form", methods=["GET", "POST"])
def requester_form():
    if request.method == "POST":
        if request.form.get("requester_id"):
            # Update requester data if requester_id is provided
            requester_id = request.form.get("requester_id")
            name = request.form.get("name")
            email = request.form.get("email")
            contact = request.form.get("contact")
            department = request.form.get("department")
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE requester_new SET name=?, email=?, contact=?, department_id=? WHERE requester_id=?", (name, email, contact, department, requester_id))
                conn.commit()
            return redirect(url_for("review_forms"))
        else:
            # Insert new requester data
            name = request.form.get("name")
            email = request.form.get("email")
            contact = request.form.get("contact")
            department = request.form.get("department")
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO requester_new (name, email, contact, department_id) VALUES (?, ?, ?, ?)", (name, email, contact, department))
                conn.commit()
            # Fetch the inserted requester data
            cursor.execute("SELECT * FROM requester_new WHERE email=?", (email,))
            requester_data = cursor.fetchone()
            # Redirect to the project_info route with requester_id as a parameter
            return redirect(url_for("project_info", requester_id=requester_data[0]))
    else:
        # Fetch department data from the database and pass it to the template
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT department_id, name FROM department_new")
            departments = cursor.fetchall()
        return render_template("requester_form.html", departments=departments)

# Define the project_info route
@app.route("/project_info", methods=["GET", "POST"])
def project_info():
    if request.method == "POST":
        if request.form.get("project_id"):
            # Update project info if project_id is provided
            project_id = request.form.get("project_id")
            project_title = request.form.get("project_title")
            output = request.form.get("output")
            objective = request.form.get("objective")
            recipient = request.form.get("recipient")
            mandatory = request.form.get("mandatory_text")
            date_filed = request.form.get("date_filed")
            date_needed = request.form.get("date_needed")
            additional_info = request.form.get("additional_info")
            status_id = "active"  # Set status ID to active
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE project_info_new1 SET project_title=?, output=?, objective=?, recipient=?, mandatory=?, date_filed=?, date_needed=?, add_info=?, status_id=? WHERE project_id=?", (project_title, output, objective, recipient, mandatory, date_filed, date_needed, additional_info, status_id, project_id))
                conn.commit()
            return redirect(url_for("review_forms"))
        else:
            # Insert new project info
            project_title = request.form.get("project_title")
            output = request.form.get("output")
            objective = request.form.get("objective")
            recipient = request.form.get("recipient")
            mandatory = request.form.get("mandatory")
            date_filed = request.form.get("date_filed")
            date_needed = request.form.get("date_needed")
            additional_info = request.form.get("additional_info")
            status_id = "active"  # Set status ID to active
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO project_info_new1 (project_title, output, objective, recipient, mandatory_text, date_filed, date_needed, add_info, status_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (project_title, output, objective, recipient, mandatory, date_filed, date_needed, additional_info, status_id))
                conn.commit()
            return redirect(url_for("home"))  
    else:
        return render_template("project_info.html")

# Define the admin_login route
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        return redirect(url_for("review_forms"))  
    else:
        return render_template("admin_login.html")

# Define the review_forms route
@app.route("/review_forms", methods=["GET", "POST"])
def review_forms():
    sort_order = request.args.get('sort_date', 'asc')  # Get the sorting order from the query parameter
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requester_new")
        requester_data = cursor.fetchall()
        cursor.execute("SELECT * FROM project_info_new1")
        project_info_data = cursor.fetchall()

    # Sort the data based on the "Date Needed" column
    project_info_data.sort(key=lambda x: x[9], reverse=(sort_order == 'desc'))

    zipped_data = zip(requester_data, project_info_data)
    
    return render_template("review_forms.html", zipped_data=zipped_data)


# Define the delete route
@app.route("/delete", methods=['POST'])
def delete():
    requester_id = request.form['requester_id']
    project_id = request.form['project_id']
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM requester_new WHERE requester_id=?", (requester_id,))
            cur.execute("DELETE FROM project_info_new1 WHERE project_id=?", (project_id,))
            con.commit()
            msg = "Record successfully deleted from the database"
    except Exception as e:
        con.rollback()
        msg = f"Error in the DELETE: {str(e)}"
    finally:
        con.close()
    return redirect(url_for("review_forms"))  

# Define the personnel route
@app.route("/personnel", methods=["GET", "POST"])
def personnel():
    if request.method == "POST":
        # If the form is submitted, add the new personnel data to the database
        name = request.form.get("name")
        email = request.form.get("email")
        role = request.form.get("role")  # Get the selected role from the form
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            # Insert the name, email, and role into the personnel table
            cursor.execute("INSERT INTO personnel_new (name, email, role_id) VALUES (?, ?, ?)", (name, email, role))
            conn.commit()
    
    # Fetch the updated personnel list from the database
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personnel_new")
        personnel_list = cursor.fetchall()
        
    # Pass the personnel list to the personnel.html template
    return render_template("personnel.html", personnel_list=personnel_list)

if __name__ == "__main__":
    app.run(debug=True)
