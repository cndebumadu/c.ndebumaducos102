name  = input(" what is your name: ")
age = int(input("how old are you? "))
yoe = int(input("how many years of work experience do you have?  "))
if yoe > 25 and age>= 55:
    print( "{name} your average tax revenue is 5,600,000 ")
elif yoe > 20 and age>= 45:
    print( "your average tax revenue is 4,480,000")
elif yoe > 10 and age >= 35:
    print("your average tax revenue is 1,500,000")
else:
    print( "your average tax revenue is 550,000")




