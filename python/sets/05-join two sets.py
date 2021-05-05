# join two sets 
set1 = {"a,","b","c"}
set2 = {1,2,3}
# union()
set3 =set1.union(set2)
print(set3)

# update()

set3.update(set1)
print(set3)

# The intersection_update() method will keep only the items that are present in both sets.

x = {1,2,3}
y = {3,4,5}
x.intersection_update(y)
print(x)

# intersection() will only keep item present in both sets 

x.intersection(y)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x.symmetric_difference_update(y)
print(x)
# create a new set but as same as symetric_difference_update
x.symmetric_difference(y)
print(x)