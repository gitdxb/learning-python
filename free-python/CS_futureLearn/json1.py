import json
'''
data = {
    "Name": "Neil Armstrong",
    "Age": 82,
    "Hobbies": ["Aircraft design", "Fishing", "Astronaut"]
}
with open("neil.json","w") as f:
    json.dump(data,f)
'''

with open("neil.json","r") as f:
    data2 = json.load(f)
print(data2)