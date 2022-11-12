from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import db

#Initialize app
app = Flask(__name__)

local_session = db.Session(bind=db.engine)

# home route
@app.route('/')
def index():
    results = local_session.query(db.Courses).all()
    for r in results:
        print(r.name)
    return render_template("index.html", courses=results)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get("name")
    number = request.form.get("number")
    credit_hours = request.form.get("hours", type=int)
    return "<div>" + name + " " + number + " " + str(credit_hours) + "</div>"

local_session.close()
if __name__ == '__main__':
    app.run(debug=True, threaded=False)