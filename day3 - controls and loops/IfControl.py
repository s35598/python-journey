#IfControl

Age = int(input("Enter your age: "))
if Age < 0 or Age > 100:
    print("Enter a valid age")
elif Age >= 18:
    print("Your can buy alcohol!")
else:
    print("Your can not buy alcohol! You must wait more" , 18-Age , "years.")