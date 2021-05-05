fruits = ("apple", "banana", "cherry")

(green,yellow,red) = fruits

print(green)
print(yellow)
print(red)

# using astric * when variables on lhs is less than the item in tuple in rhs, we use astric to give remaining values to last variable assigned

(green,*red) = fruits
print(red)