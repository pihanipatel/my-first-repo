## Q - 1
# First_name = input("please enter your first name: ")
# Last_name = input("please enter your last name: ")
# print("Hello", Last_name, First_name+"!")
# print("Hello {} {}!".format(Last_name,First_name))
# print("Hello %s %s!"%(Last_name,First_name))

# ## Q - 2
# item = "apple"
# price = 5.50
# print(f"The price of {item} is {price} dollars.")

# ## Q - 3
# name = input("Please enter your name: ")
# reverse = name[::-1]
# if(reverse == name):
#     print("string is palindrome.")
# else:
#     print("string is not palindrome.")    

# ## Q - 4
# user = input("Please enter your favourite string: ")
# upp = user.upper()
# print(upp)   
# low = user.lower()
# print(low)   
# title = user.title()
# print(title)    

# ## Q - 5
# str = "Machine Learning and AI are trending."
# new_str = str.replace("AI","Artificial Intelligence")
# print(new_str)

# string = "data data mining and big data."
# updated = string.count("data")
# print(updated)

# ## Q - 6
str = "apple,banana,grapes"
list = []

list = str.split(",")
print(list)   

ilist = []
list = ["Python","is","awesome"]
for i in list:
    ilist = " ".join(list)
print(ilist)

str = ["Python",
"Java",
"c",
"c++"]
sen = []  
for i in str:      
    i.split(",")
    print(i)

## Q - 7
str = "Hello Python World"
print(str.startswith("Hello"))
print(str.endswith("World"))

text = "Data123#Science!"
tex = ""
for i in text:
    if i.isalpha():
        tex += i
print(tex)


str = "Python"        
reversed = str[::-1]
print(reversed)