#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:57:42 2023

@author: manuelperrin
"""

import json
import sqlite3
import base64

def compare_message_to_json(message_id, json_file, database_file):
    
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE id=?", (message_id,))
    row = cursor.fetchone()

    cursor.execute("SELECT name FROM contact WHERE id=?", (row[4],))
    contact_name = cursor.fetchone()[0]
    
    json_data = {
        "id": row[0],
        "timestamp": row[1],
        "direction": row[2],
        "content": base64.b64encode(row[3].encode('utf-8')).decode('utf-8'),
        "contact": contact_name
    }

    # Chargement du fichier JSON
    with open(json_file, 'r') as f:
        expected_data = json.load(f)

    if expected_data==json_data:
        print("True")
    else:
        print("False")


compare_message_to_json(1, "message1.json", "messaging.db")
