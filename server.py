from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import db
import unidecode

#Initialize app
app = Flask(__name__)



# home route
@app.route('/')
def index():
    # render the courses
    courses = []
    conn = db.connection()
    cursor = conn.cursor()

    # query all of the courses name
    cursor = cursor.execute("SELECT name FROM Courses")
    for row in cursor:
        courses.append(row[0])
    #print(courses)

    cursor = cursor.execute("SELECT term, year FROM Terms")
    terms = cursor.fetchall()
    conn.close()
    return render_template("index.html", courses=courses, terms=terms)

@app.route('/add/term', methods=['POST'])
def add_term():
    conn = db.connection()
    cursor = conn.cursor()

    # process form submission
    term = request.form.get("term")
    year = request.form.get("year", type=int)
    # credit_hours = request.form.get("hours", type=int)
    print(year)
    cursor.execute("INSERT INTO Terms (term, year) VALUES (?, ?)",
                    (term, year))
    conn.commit()
    conn.close()
    # # add to the database
    # new_course = StudentRegistration(course_name=name, 
    #                                  course_number=number, 
    #                                  credit_hours=credit_hours)
    # db_server.session.add(new_course)
    # db_server.session.commit()
    return redirect(url_for('index'))

# add route
@app.route('/add/course', methods=['POST'])
def add_course():
    # process form submission
    # name = request.form.get("name")
    # number = request.form.get("number")
    # credit_hours = request.form.get("hours", type=int)
    
    # # add to the database
    # new_course = StudentRegistration(course_name=name, 
    #                                  course_number=number, 
    #                                  credit_hours=credit_hours)
    # db_server.session.add(new_course)
    # db_server.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, threaded=False)


# local_session = db.Session(bind=db.engine)

# # establish database connection to the server
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db_server = SQLAlchemy(app)

# class Term(db_server.Model):
#     id = db_server.Column(db_server.Integer, primary_key=True)
#     term = db_server.Column(db_server.String(100))
#     year = db_server.Column(db_server.Integer)
#     courses = db_server.relationship('StudentRegistration', backref='term')

# class StudentRegistration(db_server.Model):
#     id = db_server.Column(db_server.Integer, primary_key=True)
#     course_name = db_server.Column(db_server.String(100))
#     course_number = db_server.Column(db_server.String(100))
#     credit_hours = db_server.Column(db_server.Integer)
#     term_id = db_server.Column(db_server.Integer, db_server.ForeignKey('term.id'))