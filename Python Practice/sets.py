# Create an empty set
s = set()

# Add elements to the set
s.add(1)
s.add(2)   
s.add(3)
s.add(4)
s.add(3) #Even while adding a number to it, it doesn't show since the number is reoccurence

s.remove(2) #This remove this particulare number "2" from the set

print(f"The set has {len(s)} elements.")