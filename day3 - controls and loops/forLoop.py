#for loop
my_string = "eren kilic"

for c in my_string:
    print(c)

my_tuple = (10,20,30,40,50)
for number in my_tuple:
    print(int(number / 5 * 2))

#tuple unpacking
my_new_list = [("a","b"),("c","d"),("e","f")]
for (x,y) in my_new_list:
    print(y)

my_dictionary = {"a":100,"b":200,"c":300,"d":400}
for (key,value) in my_dictionary.items():
    print(value)

#continue - break - pass

my_list = [1,2,3,4,5,6,7,8,9,10]

for x in my_list:
    print(x)
    if x >= 5:
        print("hello")
        break

for y in my_list:
    if y == 6:
        continue
    print(y)

for num in my_list:
    pass # daha çok bitirilmemiş kodlarda kullanılır hata almamak için.

