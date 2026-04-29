#!/usr/bin/env python3

import pymysql
import json

print("Content-Type: application/json\n")

conn = pymysql.connect(
    host="localhost",
    user="appuser",
    password="1234",
    database="contactdb"
)

cursor = conn.cursor()
cursor.execute("SELECT name, telephone FROM contacts")

data = []
for row in cursor.fetchall():
    data.append({
        "name": row[0],
        "telephone": row[1]
    })

result = {
    "ok": True,
    "count": len(data),
    "data": data
}

print(json.dumps(result))

conn.close()
