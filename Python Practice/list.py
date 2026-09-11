#DATA STRUCTURES
# Define a list of names
names = ["Harry ", "Ron", "Hermione ", "Ginny "]

#names[2]="Sherif" This changes the name shown on the second sequence of list

names.append("Draco") #This added or append name "Draco" to the end of the existing lists

names.sort() #This sort the names alphabetically ordered

#names.pop(0) #This removes the first name in the list. If you left empty, it defaults to removing the last item.

#names.remove("Ron") #This removes the name "Ron" from the list

#names.insert(1, "Hermione") #This inserts the name "Hermione" at index 1

#names.extend(["Luna", "Neville"]) #This adds the names "Luna" and "Neville" to the end of the existing list

#index = names.index("Draco") #This finds the index of the name "Draco" in the list
#print(index)

# count = names.count("Sherif") #This counts the number of times the name "Harry" appears in the list
# print(count)

print(names)