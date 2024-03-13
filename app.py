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
        department_id = request.form.get("department_id")  # Assuming you have a department dropdown or input
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO requester (name, email, department_id, contact) VALUES (?, ?, ?, ?)", (name, email, department_id, contact))
            conn.commit()
        return redirect(url_for("project_info"))
    else:
        # Render the requester form page
        return render_template("requester_form.html")

@app.route("/project_info", methods=["GET", "POST"])
def project_info():
    if request.method == "POST":
        # Handle form submission for project info
        project_id = request.form.get("project_id")
        requester_id = request.form.get("requester_id")
        output = request.form.get("output")
        objective = request.form.get("objective")
        date_filed = request.form.get("date_filed")
        date_needed = request.form.get("date_needed")
        additional_info = request.form.get("additional_info")
        admin_id = request.form.get("admin_id")
        status_id = request.form.get("status_id")
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO project_info (project_id, requester_id, output, objective, date_filed, date_needed, add_info, admin_id, status_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (project_id, requester_id, output, objective, date_filed, date_needed, additional_info, admin_id, status_id))
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
        cursor.execute("SELECT * FROM requester")
        requester_data = cursor.fetchall()
        cursor.execute("SELECT * FROM project_info")
        project_info_data = cursor.fetchall()
    return render_template("review_forms.html", requester_data=requester_data, project_info_data=project_info_data)

if __name__ == "__main__":
    app.run(debug=True)