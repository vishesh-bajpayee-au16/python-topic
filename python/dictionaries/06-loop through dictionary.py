thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print all keys 
for x in thisdict:
    print(x)

# or

for x in thisdict.keys():
    print(x)

# print all values

for x in thisdict:
    print(thisdict[x])

# or

for x in thisdict.values():
    print(x)


# loop through both keys and items 

for x, y in thisdict.items():
    print(x,y)