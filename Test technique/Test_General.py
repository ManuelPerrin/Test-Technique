#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:00:05 2023

@author: manuelperrin
"""

import json

expected_fields = {
    "id": int,
    "timestamp": int,
    "direction": str,
    "content": str,
    "contact": str,
    }

def test(json_file):
    with open(json_file, 'r') as f:
        json_data=json.load(f)
    for field, field_type in expected_fields.items():
        if field not in json_data:
            print(f"Le champ '{field}' est manquant dans le fichier JSON.")
            return False
        if not isinstance(json_data[field], field_type):
            print(f"Le champ '{field}' n'est pas au format attendu.")
            return False
    if json_data['direction'] not in ['originating', 'destinating']:
        print("La valeur du champ 'direction' doit être soit 'originating' soit 'destinating'.")
        return False
    return True


if test("message1.json"):
    print("Le fichier JSON est conforme.")
else:
    print("Le fichier JSON n'est pas conforme.")
