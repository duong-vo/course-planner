from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import sessionmaker
import time
import db

# create a connection with the database
conn = db.connection()
cursor = conn.cursor()

url = "https://bulletin.miamioh.edu/engineering-computing/computer-science-bs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr', class_=['even', 'odd'])
cheat_credit_hours = 3
for ele in lists:
    course_name_raw = ele.find("a", class_="bubblelink code")
    if course_name_raw:
        course_name = course_name_raw.text
        try:
            cursor.execute("INSERT INTO Courses (name, hours) VALUES (?, ?)", (course_name, cheat_credit_hours))
            conn.commit()
        except:
            pass

conn.close()