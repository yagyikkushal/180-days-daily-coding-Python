# Convert JSON Data to Python Object

json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'

import json

py_obj = json.loads(json_obj)
print(py_obj)

print(py_obj["Name"])