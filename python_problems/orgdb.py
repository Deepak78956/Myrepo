'''
This program creates a SQLite DataBase conataining the name
 and the number of Organisations in the data.txt file
'''
import sqlite3
conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Counts")  #To delete the pre-existed table every time the program runs
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")  # This creates a table named Counts
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    ls = email.split('@')
    orgn = ls[1]
    cur.execute("SELECT * FROM Counts WHERE org = ?", (orgn,))  # It retreives the record, you have to retrieve the record before fetching
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (orgn,)) # If oraganisation doesn't exists it creates the one and sets its count to 1
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (orgn,))  # If oraganisation exists it adds count to count + 1
conn.commit()
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC"
for row in cur.execute(sqlstr):
    print(row[0], row[1])
cur.close()

