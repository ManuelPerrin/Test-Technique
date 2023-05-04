#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:10:25 2023

@author: manuelperrin
"""

import sqlite3
import json

# définition des champs requis pour chaque message
expected_fields = {
    "id": int,
    "timestamp": int,
    "direction": str,
    "content": str,
    "contact": str
}

# connexion à la base de données SQLite
conn = sqlite3.connect('messaging.db')

# extraction des données de la base de données
cursor = conn.cursor()
cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()

# vérification de chaque enregistrement
for row in rows:
    cursor.execute("SELECT name FROM contact WHERE id=?", (row[4],))
    name=cursor.fetchone()[0]
    # conversion de l'enregistrement en un objet JSON
    json_data = {
        "id": row[0],
        "timestamp": row[1],
        "direction": row[2],
        "content": row[3],
        "contact": str(name)
    }

    #Vérification du fichier JSON
    try:
        json.loads(json.dumps(json_data))
    except ValueError:
        print(f"L'enregistrement {row[0]} n'est pas un objet JSON valide")
        continue

    # vérification des champs requis et de leurs types
    for field, field_type in expected_fields.items():
        if field not in json_data:
            print(f"L'enregistrement {row[0]} ne contient pas le champ '{field}'")
            continue
        if not isinstance(json_data[field], field_type):
            print(f"Le champ '{field}' de l'enregistrement {row[0]} doit être de type {field_type.__name__}")