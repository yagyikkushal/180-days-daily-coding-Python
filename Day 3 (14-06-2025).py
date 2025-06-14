# Write a Python program to convert a nested JSON string into a Python dictionary and extract a specific nested value.

json_string = '''
{
    "student": {
        "name": "Kushal",
        "age": 25,
        "address": {
            "city": "Kanpur",
            "zipcode": "208001"
        },
        "marks": {
            "math": 90,
            "science": 88
        }
    }
}
'''

import json

py_obj = json.loads(json_string)
print(py_obj)

print(py_obj["student"]["address"]["city"])



