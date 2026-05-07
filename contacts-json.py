#!/usr/bin/env python3

import pymysql
import json

print("Content-Type: application/json\n")

try:
    conn = pymysql.connect(
        host="localhost",
        user="appuser",
        password="1234",
        database="contactdb"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT name, telephone, email, address FROM contacts")

    data = []
    for row in cursor.fetchall():
        data.append({
            "name": row[0],
            "telephone": row[1],
            "email": row[2],
            "address": row[3]
        })

    print(json.dumps({
        "ok": True,
        "count": len(data),
        "data": data
    }))

    conn.close()

except Exception as e:
    print(json.dumps({
        "ok": False,
        "error": str(e)
    }))