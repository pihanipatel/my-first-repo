## Q - 1
num1,num2,num3 = 3,7,5
if num1 > num2:
    if num1 > num3:
        print("largest number is: ",num1)
if num2 > num1:
    if num2 > num3:
        print("largest number is: ",num2)
if num3 > num1:
    if num3 > num2:
        print("largest number is: ",num3)
                        
## Q - 2
num1,num2,num3 = 3,7,5
if num1 < num2:
    if num1 < num3:
        print("minimum number is: ",num1)
if num2 < num1:
    if num2 < num3:
        print("minimum number is: ",num2)
if num3 < num1:
    if num3 < num2:
        print("minimum number is: ",num3)
                        
# Q - 3
num1,num2,num3,num4 = 3,7,5,8
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("largest number is: ",num1)
if num2 > num1:
    if num2 > num3:
        if num2 > num4:
            print("largest number is: ",num2)
if num3 > num1:
    if num3 > num2:
        if num3 > num4:
            print("largest number is: ",num3)
if num4 > num1:
    if num4 > num2:
        if num4 > num3: 
            print("largest number is: ",num4)   

## Q - 4

operator = input("please enter operator: ")   
a = int(input("please enter number1: "))     
b = int(input("please enter number2: "))     
match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")     
    case _:
        print("Invalid operator")

## Q - 5
num = int(input("Please enter number: "))
match num:
    case 1:
        print("Sandwich")
    case 2:
        print("Pizza")
        match num:
            case 1:
                print("Thin Crust Pizza")
            case 2:
                print("Cheese Burst Pizza")
            case 3:
                print("Fresh Dough Pizza") 
    case 3:
        print("Burger")        
    case _:
        print("Invalid number")

## Q - 6
num = int(input("please enter number: "))
match num:
    case 1:
        print("English")
        match num:
            case 1:
                print("basic")
            case 2:
                print("Advance")    
    case 2:
        print("Hindi")    
    case 3:
        print("Gujarati")   
    
