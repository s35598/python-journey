#loops - for loop, while loop

myList = [10,15,20,30,34,40,47,50,60,70]

print("Numbers can divided by six: ")
for number in myList:
    if number % 6 == 0:
        print(number)

print("odd numbers: " )
for number in myList:
    if number % 2 != 0:
        print(number)


