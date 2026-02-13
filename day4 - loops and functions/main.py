#range
for i in range(0,10,1):
    if i == 3:
        continue  #  (sadece o turu atlar)
    if i == 5:
        break     # (döngüyü tamamen kırar)
    print(i)

print("list loop")
#list loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while loop
x = 0
while x < 4:
    print(x)
    x = x + 1


sum = 0
for i in range(2):
    num = int(input("Enter a number: "))
    sum += num
print(f"Sum of the numbers: {sum}")  # aynı zamanda ("Sum of the numbers: ", {sum}) de kullanılır ikiside aynı işlevde