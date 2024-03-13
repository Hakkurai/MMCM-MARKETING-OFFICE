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
        return "Invalid role"

@app.route("/requester_form", methods=["GET", "POST"])
def requester_form():
    if request.method == "POST":
        if request.form.get("requester_id"):
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
            name = request.form.get("name")
            email = request.form.get("email")
            contact = request.form.get("contact")
            department = request.form.get("department")
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO requester_new (name, email, contact, department_id) VALUES (?, ?, ?, ?)", (name, email, contact, department))
                conn.commit()
            return redirect(url_for("project_info"))
    else:
        return render_template("requester_form.html")

@app.route("/project_info", methods=["GET", "POST"])
def project_info():
    if request.method == "POST":
        if request.form.get("project_id"):
            project_id = request.form.get("project_id")
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
                cursor.execute("UPDATE project_info_new1 SET project_title=?, output=?, objective=?, recipient=?, mandatory=?, date_filed=?, date_needed=?, add_info=?, status_id=? WHERE project_id=?", (project_title, output, objective, recipient, mandatory, date_filed, date_needed, additional_info, status_id, project_id))
                conn.commit()
            return redirect(url_for("review_forms"))
        else:
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
                cursor.execute("INSERT INTO project_info_new1 (project_title, output, objective, recipient, mandatory, date_filed, date_needed, add_info, status_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (project_title, output, objective, recipient, mandatory, date_filed, date_needed, additional_info, status_id))
                conn.commit()
            return redirect(url_for("home"))  
    else:
        return render_template("project_info.html")

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        return redirect(url_for("review_forms"))  
    else:
        return render_template("admin_login.html")

@app.route("/review_forms")
def review_forms():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requester_new")
        requester_data = cursor.fetchall()
        cursor.execute("SELECT * FROM project_info_new1")
        project_info_data = cursor.fetchall()
        
    zipped_data = zip(requester_data, project_info_data)
    
    return render_template("review_forms.html", zipped_data=zipped_data)

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

if __name__ == "__main__":
    app.run(debug=True)
