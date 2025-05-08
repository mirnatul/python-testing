import json

json_data = '{"name": "Alice", "age": 25, "is_student": false}'
python_dict = json.loads(json_data)  # type is dict

# json_data = json.dumps(python_dict)  # type is str


# prettify json output
json_data = json.dumps(python_dict, indent=4)
# tuple of (item separator, key separator)
json_data = json.dumps(python_dict, separators=(",", ":"))
# sort alphabetically
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

print(json_data)
