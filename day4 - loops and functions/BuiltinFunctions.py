#enumerate
myList = [10,20,30,40,50]
for (ix,value) in enumerate(myList):
    print(ix,value)

#random

from random import randint
randomNumber = randint(0,100)
print(randomNumber)
from random import shuffle

shuffle(myList)
print(myList)

print(myList[randint(0,len(myList)-1)])

#zip

food_list = ["apple", "banana", "cherry"]
calories_list = [100,200,300]
day_list = ["monday", "tuesday", "wednesday"]
zippedList = list(zip(food_list,calories_list,day_list))
print(zippedList)

#list comprehension

new_list = []
my_string = "metallica"
new_list = [element for element in my_string]
print(new_list)

number_list = [10,20,30,40,50]
new_number_list = [num/2 for num in number_list]
print(new_number_list)

# new_number_list = []       --> bu sekilde de yazılabilirdi aynı islevdeler
# for num in number_list:
# new_number_list.append(num/2)

metal_list = ["metallica","iron maiden","dream theater","megadeth","ac/dc"]
print(metal_list[randint(0,len(metal_list)-1)])
