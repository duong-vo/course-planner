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
        courses.append(row[0].replace(u"\xa0", " "))
    print(courses)
    # query all terms
    cursor = cursor.execute("SELECT id, term, year FROM Terms")
    terms = cursor.fetchall()

    # query all of the student courses
    cursor = cursor.execute("SELECT termId, name, hours FROM StudentCourses")
    student_courses = cursor.fetchall()

    conn.close()
    return render_template("index.html", courses=courses, 
                                         terms=terms,
                                         student_courses=student_courses)

@app.route('/add/term', methods=['POST', 'GET'])
def add_term():
    if request.method == 'POST':
        conn = db.connection()
        cursor = conn.cursor()

        # process form submission
        term = request.form.get("term")
        year = request.form.get("year", type=int)
        cursor.execute("INSERT INTO Terms (term, year) VALUES (?, ?)",
                        (term, year))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template("add_term.html")

# add route
@app.route('/add/course/<int:term_id>', methods=['POST', 'GET'])
def add_course(term_id):
    if request.method == 'POST':
        conn = db.connection()
        cursor = conn.cursor()
    
        # process form submission
        raw_name = request.form.get("name")
        number = request.form.get("number")
        name = raw_name + " " + number
        hours = request.form.get("hours", type=int)
        print(term_id)
        # add to the database
        cursor.execute("""INSERT INTO StudentCourses (termId, name, hours)
                             VALUES (?, ?, ?)""", (term_id, name, hours))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template("add_course.html", term_id=term_id)

# Delete route
@app.route('/delete/term/<int:term_id>')
def delete_term(term_id):
    conn = db.connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Terms WHERE id=%s                  
                   """ % (term_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Delete route
@app.route('/delete/course/<int:course_id>')
def delete_course(course_id):
    conn = db.connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM StudentCourses WHERE termId=%s                  
                   """ % (course_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


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