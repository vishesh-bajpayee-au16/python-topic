# SORT LISTS ALPHANUMERICALLY

the_list = ["apple","banana","orange","mango"]
the_list.sort()
print(the_list)
num_list = [100,50,65,82,23]
num_list.sort()
print(num_list)

# SORT DESCENDING 
num_list.sort(reverse = True)
print(num_list)

# CUSTOMISED SORT FUNCTION

def myFunction(n):
    return abs(n-50)

num_list.sort(key = myFunction)
print(num_list)

# CASE SENSETIVE SORT 
the_list.sort(key = str.lower)

# REVERSE ORDER

the_list.reverse()
print(the_list)