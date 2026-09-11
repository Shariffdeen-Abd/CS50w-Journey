# houses = {"Harry": "Gryffindor", "Mubashir": "Abuja"} #Dictionaries store data in Key-Value pairs {Key: Value}.

# houses["Sherif"] = "Abuja"; #This takes the houses dict and look up to Abuja and it'll be set to the house of Sherif which adds it to Abuja
# print(houses["Sherif"])

# Start your dictionary values as lists []
houses = {
    "Harry": "Gryffindor", "Mubashir": "Abuja"
}

# 1. Look up Harry's list and append a second value to it
houses["Harry"] = "Slytherin"

# 2. Add a new person with a list value, then add to it later
houses["Sherif"] = ["Abuja"]
houses["Sherif"].append("London")

print(houses)

# details = {
#     "name": "Sherif", "age": "19"
# }

# print(details)