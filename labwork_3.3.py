## Q - 1
num = int(input("please enter number: "))
while num != 0:
    print(num)
    num = int(input("please enter number: "))
print("loop ended because you entered 0")

## Q - 2
for i in range(1,11):
    print(i*i)

# Q - 3

num = 2
while num <= 51:
    if num % 2 == 0:
        print("All even numbers between 1 and 50: ",num)
    num += 1

## Q - 4

for i in range(1,21,1):
    print(i)
for i in range(1,21,1):
    if i % 2 != 0:
        print(i)    

## Q - 5

for i in range(5,50,5):
    print(i)

## Q - 6

for i in range(10,0,-1):
    print(i)

## Q - 7

for i in range(1,51,1):
    if i % 2 == 0:
        print("Divisible by 2")
    elif i % 3 == 0:
        print("Divisible by 3")
    elif i % 2 == 0 or i % 3 == 0:
        print("Divisible by both")
    else:
        print(" Not Divisible by 2 or 3")            