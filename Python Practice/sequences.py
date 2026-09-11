#Storing One Name and Printing a letter out of the name
name = "Harry" #This is a Variable

print(name[0]) #The square bracs enhanced the sequence of the variable "Harry"

#In a nutshell, sequence is made use of using a square braces

#Storing One Name and Printing a name
name = ["Harry"] #This is a Variable

print(name[0]) #The square braces enhanced the sequence of letter of the variable "Harry"

#Storing Multiple Names and print a Name out of it using a sequence []
names = ["Harry ", "Ron", "Hermione"]

#Swaps the name "Ron" with "Draco"
names[1]="Draco"
print(names[1]) #This is a list and it is mutable

#Storing Multiple Names and print all the names using the variable names
names = ["Harry ", "Ron", "Hermione"]
print(names)

#Tuple
coordinateX = 10.0
coordinateY = 20.0

coordinate = (10.0, 20.0)

print(coordinate[1]) #This is a tuple and it is immutable

#Sequence can be changed or modified (mutable) while Tuple cannot be changed or modified (Immutable)