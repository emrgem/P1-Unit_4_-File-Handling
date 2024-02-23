import json
# #JSON string
# json_string = '{"name": "John", "age": 30, "city": "New York"}'
# print(type(json_string))
# #Parsing JSON string into a Python Dictionary - json.loads()
# python_data = json.loads(json_string)
# print(python_data)
# print(type(python_data))

# #Python Dictionary
# python_dict = {
#     "name": "Alicia",
#     "age": 16,
#     "city": "Teterboro"
# }
# #Convert Python dict into a JSON string - json.dumps()
# json_string = json.dumps(python_dict)
# print(type(json_string))

path = "states.json"
# with open(path) as jsonFile:
#     data = json.load(jsonFile)
#     # print(type(data))
#     for state in data["states"]:
#         # print(state)
#         # print(state['name'])
#         print(state['name'],state['abbreviation'])
with open(path) as jsonFile:
    data = json.load(jsonFile)
    for state in data['states']:
        del state['area_codes']
    print(data)
    with open("new_states.json", 'w') as newJson:
        json.dump(data,newJson,indent=2,sort_keys=True)