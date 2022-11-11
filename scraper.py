from bs4 import BeautifulSoup
import requests
import db
from sqlalchemy.orm import sessionmaker

# new session
Session = sessionmaker(bind=db.engine)
session = Session()

url = "https://bulletin.miamioh.edu/engineering-computing/computer-science-bs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr', class_=['even', 'odd'])
course_names = []
cheat_credit_hours = int(3)
for ele in lists:
    course_name = ele.find("a", class_="bubblelink code")
    if course_name:
        #print(course_name.text)
        course = db.Courses(course_name.text, cheat_credit_hours)
        session.add(course)

session.commit()


