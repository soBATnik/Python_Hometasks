# Task_2
import json
import sys


file_path = "PHONEBOOK.json"

PHONEBOOK = []

PHONE = {
    "+380630301006": 1,
    "+380932488217": 2,
    "+380667156836": 2,
    "+380958792474": 3,
    "+380509916430": 4,
}

FIRST_NAME = {
    1: "Kateryna",
    2: "Yurii",
    3: "Nataliia",
    4: "Oleh"
}

LAST_NAME = {
    1: "Kuprina",
    2: "Askin",
    3: "Dowgan",
    4: "Askinderov"
}

FULL_NAME = {
    1: "Kateryna Kuprina",
    2: "Yurii Askin",
    3: "Nataliia Dowgan",
    4: "Oleh Askinderov"
}

CITY_STATE = {
    1: "Selo City",
    2: "Selo City",
    3: "North Carolina",
    4: "Just Selo"
}

with open(file_path, 'w') as json_file:
    json.dump(PHONE, json_file)
    json.dump(FIRST_NAME, json_file)
    json.dump(LAST_NAME, json_file)
    json.dump(FULL_NAME, json_file)
    json.dump(CITY_STATE, json_file)

