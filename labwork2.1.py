## Q - 1 
num = int(input("please enter number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")    

## Q - 2
age = int(input("Please enter your age: "))
if age >= 0 and age <= 12:
    print("Child")
else:
    if age >= 13 and age <= 19:
        print("Teenager")
    else:
        if age >= 20 and age <=59:
            print("Adult")
        else:
                print("Senior")              

## Q - 3
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print("Largest number: ",num1)
elif num2 > num1 and num2 > num3:
    print("Largest number: ",num2)
else:
    print("Largest number: ",num3)        

## Q - 4
num = int(input("Please enter number: "))
if num == 0:
    print("number is neutral")
elif num == 1:
    print("number is neutral")
else:
    print("number is not neutral")    