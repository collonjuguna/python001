import sqlite3
conn = sqlite3.connect('example.db')
print("opened database successfully")
conn.execute("UPDATE EMPLOYEES SET AGE=46 WHERE ID=3")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEES")

for row in cursor:
    print("ID :", row[0])
    print("NAME ", row[1])
    print("AGE :", row[2])
    print("SALARY ", row[3])

print("Update done successfully")
conn.close()