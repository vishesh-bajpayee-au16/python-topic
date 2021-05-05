thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
# if item doesnot exist removewill raise an error
# using discard() for removing elements 
# if item doesnt exist, discard will not reaise an error
thisset.discard("banana")
print(thisset)

# clear() to empty the set 
thisset.clear()

# del to delee set completely

del thisset