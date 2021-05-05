# Add items 

thisset = {"apple","banana","mango"}

thisset.add("cherry")
print(thisset)

# add sets from another set 
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# add any iterable 
mylist = (1,2,3,4,5)
thisset.update(mylist)
print(thisset)

