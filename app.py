from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        cursor = db.cursor()
        cursor.execute("INSERT INTO mytable (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        cursor.close()
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
