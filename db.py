# from sqlalchemy import create_engine
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.pool import SingletonThreadPool
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///db.sqlite', echo=True, 
#                         poolclass=SingletonThreadPool)
# base = declarative_base()

# Session = sessionmaker()

# class Courses (base):
#     __tablename__ = 'courses'
#     name = Column(String, primary_key=True)
#     hours = Column(Integer)
    
#     def __init__(self, name, hours):
#         self.name = name
#         self.hours = hours
# engine.dispose()
# base.metadata.create_all(engine)

import sqlite3

# create a new database connection
def connection():
    try:
        conn = sqlite3.connect('planner.db')
    except sqlite3.error as e:
        print(e)
    return conn
# create a cursor

conn = connection()
cursor = conn.cursor()

# Create Terns table
cursor.execute("""CREATE TABLE IF NOT EXISTS Terms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    term VARCHAR(255) NOT NULL,
                    year INTEGER
                    );""")

# Create the available courses table
cursor.execute("""CREATE TABLE IF NOT EXISTS Courses (
                    name VARCHAR(255) PRIMARY KEY,
                    hours INTEGER
                    );""")

# Create the student courses table
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentCourses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    termId INTEGER,
                    name VARCHAR(255) NOT NULL,
                    hours INTEGER
                    );""")

conn.close()