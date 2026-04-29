#!/usr/bin/env python3

import pymysql

print("Content-Type: text/html\n")

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="appuser",
    password="1234",   # leave empty for GCP default
    database="contactdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name, telephone, email FROM contacts")

print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Contacts</title>
<style>
body {
    font-family: Arial;
    background: #f5f5f5;
}
table {
    border-collapse: collapse;
    width: 50%;
    margin: 50px auto;
    background: white;
}
th {
    background: #4CAF50;
    color: white;
    padding: 10px;
}
td {
    padding: 10px;
}
tr:nth-child(even) {
    background: #f2f2f2;
}
</style>
</head>
<body>

<h2 style="text-align:center;">Contact List</h2>
<table>
<tr><th>Name</th><th>Phone Number</th></tr>
""")

for row in cursor.fetchall():
    print(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>")

print("""
</table>
</body>
</html>
""")

conn.close()
