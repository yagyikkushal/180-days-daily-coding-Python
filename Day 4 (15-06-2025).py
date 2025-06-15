# WAPP to parse a JSON array into a Python list and filter its elements based on a condition.
import json

json_array = '''
[
    {"name": "Kushal", "score": 92},
    {"name": "Yash", "score": 76},
    {"name": "Anya", "score": 85},
    {"name": "Ravi", "score": 68}
]
'''

py_list = json.loads(json_array)
print(py_list)
print(type(py_list))

py_list_filter = [element for element in py_list if element["score"]>80]
print(py_list_filter)

