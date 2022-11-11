from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite', echo=True)
base = declarative_base()

class Courses (base):
    __tablename__ = 'courses'
    name = Column(String, primary_key=True)
    hours = Column(Integer)
    
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

base.metadata.create_all(engine)