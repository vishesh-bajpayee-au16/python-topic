thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

# Get keys 

x = thisdict.keys()
print(x)
thisdict["car"] = 1992

# Get values 

x = thisdict.values()
print(x)

# get items 

x = thisdict.items()
print(x)

# check if key exists 

if "model" in thisdict:
    print("True")
    