import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    role = request.form.get("role")
    if role == "student":
        return redirect(url_for("requester_form"))
    elif role == "admin":
        return redirect(url_for("admin_login"))
    else:
        # Handle invalid role
        return "Invalid role"

@app.route("/requester_form", methods=["GET", "POST"])
def requester_form():
    if request.method == "POST":
        # Handle form submission for requester form
        name = request.form.get("name")
        email = request.form.get("email")
        contact = request.form.get("contact")
        department = request.form.get("department")  # corrected field name
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO requester_new (name, email, contact, department_id) VALUES (?, ?, ?, ?)", (name, email, contact, department))
            conn.commit()
        return redirect(url_for("project_info"))
    else:
        # Render the requester form page
        return render_template("requester_form.html")

@app.route("/project_info", methods=["GET", "POST"])
def project_info():
    if request.method == "POST":
        # Handle form submission for project info
        project_title = request.form.get("project_title")
        output = request.form.get("output")
        objective = request.form.get("objective")
        recipient = request.form.get("recipient")
        mandatory = request.form.get("mandatory")
        date_filed = request.form.get("date_filed")
        date_needed = request.form.get("date_needed")
        additional_info = request.form.get("additional_info")
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO project_info_new1 (project_title, output, objective, recipient, mandatory, date_filed, date_needed, add_info) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (project_title, output, objective, recipient, mandatory, date_filed, date_needed, additional_info))
            conn.commit()
        return redirect(url_for("home"))  # Redirect to home after submission
    else:
        # Render the project info form page
        return render_template("project_info.html")

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        # Handle admin login form submission
        # Check credentials and perform necessary actions
        return redirect(url_for("review_forms"))  # Redirect to review forms
    else:
        # Render the admin login page
        return render_template("admin_login.html")

@app.route("/review_forms")
def review_forms():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requester_new")
        requester_data = cursor.fetchall()
        cursor.execute("SELECT * FROM project_info_new1")
        project_info_data = cursor.fetchall()
        
    # Zipping the data together
    zipped_data = zip(requester_data, project_info_data)
    
    return render_template("review_forms.html", zipped_data=zipped_data)

@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            # Connect to the database and DELETE a specific record based on rowid
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("DELETE FROM requester_new WHERE rowid=?", (rowid,))
                # Note: Replace 'requester_new' with your actual table name

                con.commit()
                msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"
        finally:
            con.close()
    return redirect(url_for("review_forms"))  # Redirect to review forms page

if __name__ == "__main__":
    app.run(debug=True)
