import json

def create_gym_profile(name, address, phone, website):
    # Generate the ID: lowercase, spaces replaced with hyphens
    # Take the martial arts school name, make it lowercase, and then swap out the spaces for hyphens
    gym_id = name.lower().replace(" ", "-")

    # Create the dictionary that will hold the martial arts school info
    profile = {
        "id": gym_id,
        "name": name,
        "styles_taught": [],
        "address": address,
        "phone": phone,
        "links": {
            "website": website
        }
    }

    # Convert dictionary to JSON object (string)
    # return json.dumps(profile, ensure_ascii=False, indent=2)
    # Take the martial arts school info and turn it into a JSON object
    json_str = json.dumps(profile, ensure_ascii=False, indent=2)

    # The directory that will hold martial arts school info for a given city and province
    filename = f"martial_arts_schools/canada/province/city/schools/{gym_id}.json"

    # Open the file that holds martial arts school json info
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_str)  # write the info to the file

    return json_str

gym0 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}


gym1 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}

gym2 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}

gym3 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}

gym4 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}

gym5 = {
    "name": "",
    "address": "",
    "phone": "",
    "website": ""
}


# gym_json1 = create_gym_profile(gym1["name"], gym1["address"], gym1["phone"], gym1["website"])
# gym_json2 = create_gym_profile(gym2["name"], gym2["address"], gym2["phone"], gym2["website"])
# gym_json3 = create_gym_profile(gym3["name"], gym3["address"], gym3["phone"], gym3["website"])
# gym_json4 = create_gym_profile(gym4["name"], gym4["address"], gym4["phone"], gym4["website"])
# gym_json5 = create_gym_profile(gym5["name"], gym5["address"], gym5["phone"], gym5["website"])

# print(gym_json1)
# print(gym_json2)
# print(gym_json3)
# print(gym_json4)
# print(gym_json5)

