myString = "James Herflield"
print(len(myString))
print(myString[-1]) # equal to print(myString[len(myString) - 1])

name = "eren"
surname = "kilic"
fullname = name + " " + surname
print(fullname)

barcode = "ABCDE123654234"
# barcode[starting index: stopping index: stepping size]
print(barcode[3:7:1])
print(barcode[::-1])
print(barcode[::2])

x = 16
myList = [10,12,13,14,15,x]
print(myList)
myList.append(5)
myList.insert(1,50)
myList.remove(12)
print(myList)

#name_input = input("enter your name: ")
#print("Welcome " + name_input)

a = 10
print(float(a))

List1 = [[1,2,3],[4,5,6],[7,8,9]]
print(List1[1][0])



