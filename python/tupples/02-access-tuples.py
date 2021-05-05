# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative indexing 
print(thistuple[-1])

# Range of indexes  excluding the last index
print(thistuple[0:2])

# check if item exists 
if "apple" in thistuple:
    print("apple exists")