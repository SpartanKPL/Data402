import json

#json.load()

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])
    print(car["engine"])

path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.load(jsonfile)
value = json_data["ip"]

print(value)

#json.loads() takes a string and converts to dict


path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.load(jsonfile.read())
value = json_data["ip"]
