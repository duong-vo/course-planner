from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import db

#Initialize app
app = Flask(__name__)

local_session = db.Session(bind=db.engine)

# establish database connection to the server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_server = SQLAlchemy(app)

class StudentRegistration(db_server.Model):
    id = db_server.Column(db_server.Integer, primary_key=True)
    course_name = db_server.Column(db_server.String(100))
    course_number = db_server.Column(db_server.String(100))
    credit_hours = db_server.Column(db_server.Integer)

# home route
@app.route('/')
def index():
    registrations = StudentRegistration.query.all()
    results = local_session.query(db.Courses).all()
    for r in results:
        print(r.name)
    return render_template("index.html", courses=results, student_registrations=registrations)

# add route
@app.route('/add', methods=['POST'])
def add():
    # process form submission
    name = request.form.get("name")
    number = request.form.get("number")
    credit_hours = request.form.get("hours", type=int)
    
    # add to the database
    new_course = StudentRegistration(course_name=name, 
                                     course_number=number, 
                                     credit_hours=credit_hours)
    db_server.session.add(new_course)
    db_server.session.commit()
    return redirect(url_for('index'))

local_session.close()
if __name__ == '__main__':
    with app.app_context():    
        db_server.create_all()
        app.run(debug=True, threaded=False)