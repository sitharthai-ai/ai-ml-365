# import sqlite3

# conn = sqlite3.connect(":memory:")   # a temporary database that lives in memory
# cur = conn.cursor()

# cur.execute("CREATE TABLE students (name TEXT, city TEXT, marks INTEGER)")
# cur.executemany("INSERT INTO students VALUES (?, ?, ?)",[
#     ("Arun",   "Chennai", 82),
#     ("Priya",  "Madurai", 91),
#     ("Karthik","Chennai", 67),
#     ("Divya",  "Coimbatore", 74),
#     ("Rahul",  "Chennai", 95),
# ])

# query = """ SELECT name, marks
# FROM students
# WHERE city = 'Chennai';
# """

# for row in cur.execute(query):
#     print(row)


import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE students (name TEXT, city TEXT, marks INTEGER)")
cur.executemany("INSERT INTO students VALUES (?,?,?)",[
    ("Arun",   "Chennai", 82),
    ("Priya",  "Madurai", 91),
    ("Karthik","Chennai", 67),
    ("Divya",  "Coimbatore", 74),
    ("Rahul",  "Chennai", 95),
])

query = """
SELECT name, city
FROM students
WHERE marks > 80;
"""

for row in cur.execute(query):
    print(row)