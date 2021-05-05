# CREATE NEW LIST WITH EXISTING LIST
the_list = ["apple","banana","mango","orange"]
new_list = [x for x in the_list if x != "apple"]
print(new_list)

# ITERABLE
new_list = [x for x in range(10)]
print(new_list)

# EXPRESSION
upperCase_list = [x.upper() for x in the_list]
print(upperCase_list)

