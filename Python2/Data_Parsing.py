import json

#load from json file to python: json.load()
#load from json string to python: json.loads()
#write a json file: python to json: json.dump()
#converts to a json string: python to JSON: json.dumps()

with open("config.json", "r") as file:
    data = json.load(file)

print(data)
print(data["base_url"])

#Note: once loads, data is just a normal python dict. You access it exactly like any dict no json syntac needed after loading.

# writing python data to json

test_result = {
    "test_type": "Sanity",
    "no_of_TC": "18",
    "status": "PASS"
}

with open("result.json", "w") as file:
    json.dump(test_result, file, indent=4)
    #To make it human-readable (indented), add indent=4:

# loads() and dumps(): The String Versions
# Sometimes you get json as a plain string, not a file, a very common with API response.

# json string -> Dict
json_string = '{"name": "Sai", "role": "QA Engineer"}'

data = json.loads(json_string)
print(data["name"])
print(data)

# DIct -> JSON string
data = {"name": "Swaroop", "role": "SDET"}
json_str = json.dumps(data, indent=2)
print(json_str)

with open("config.json", "r") as file:
    config = json.load(file)

# page.goto(config["base_url"])
# page.set_default_timeout(config["timeout"] * 1000)




