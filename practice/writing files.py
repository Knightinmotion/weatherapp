# Python writing files (.txt, json, .csv)

import json

employee = {
    "name": "chris",
    "age": 30,
    "job": "cook",

}

file_path = "series.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee,file)
        print(f"json file '{file_path}' was created ")

except FileExistsError:
    print("That file already exists!")

