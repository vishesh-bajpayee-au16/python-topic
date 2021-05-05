# LOOP THROUGH LIST
the_list = ["apple","banana","mango","orange"]

for item in the_list:
    print(item)

# LOOP THROUGH THE INDEX NUMBERS

for i in range(len(the_list)):
    print(the_list[i])

# USING WHILE LOOP
count = 0

while count < len(the_list):
    print(the_list[count])
    count+= 1

# LOOP USING LIST COMPREHENSION
[print(x) for x in the_list]
