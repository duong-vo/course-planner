from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Initialize app
app = Flask(__name__)

# home route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get("name")
    number = request.form.get("number")
    credit_hours = request.form.get("hours", type=int)
    return "<div>" + name + number + str(credit_hours) + "</div>"

if __name__ == '__main__':
    app.run(debug=True)