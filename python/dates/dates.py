import datetime
from time import strftime, time

# Python Dates
print(datetime.datetime.now())

# Creating date objects 

new_date = datetime.datetime(2021,5,21)
print(new_date)



# The strftime() Method converts date into readable lines
week = new_date.strftime("%A")
print(new_date.strftime("%d-%B-%y"))

print(f"Day is: {week}")
