## Q - 1
# fruits = ["strawberry","banana","apple","cherry"]
# sec_last = fruits.pop(-2)
# print(sec_last)
# fruits.append("mango")
# print(fruits)
# fruits.sort()
# print(fruits)
# print(fruits[::-1])

# ## Q - 2
# numbers = (23,67,98,20,10)
# print(numbers[2])
# numbers.insert(1,45)
# print(numbers)

## Mutability
'''
tuple has imutability quality so we can not do any changes so if we try to do changes it gives attributr error
'''

## Q - 3
# numbers = (23,67,98)
# num = [23,67,98]
# num.insert(0,45)
# print(num)
# numbers.insert(0,45)
# print(numbers)

## Error attributr error

## Q - 4
list = []
for i in range (1,21,1):
    list.append(i * i)
    
print(list)

even = []
for i in range(20):
    if i % 2 == 0:
        even.append(i)
print(even)    

list = ["hello","WORLD","PyThOn"]
ilist = []
for i in list:
    list=i.lower()
    ilist.append(list)
    print(list)