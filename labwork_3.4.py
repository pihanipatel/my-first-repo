# Q - 1
for i in range (1,21):
    if i % 4 == 0:
        continue
    print(i)

## Q - 2
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# ## Q - 3
name = "PYTHON"
vowels = "AEIOU"
for ch in name:
        if ch in vowels:
            continue 
        print(ch,"\n")        
       
# # ## Q - 4
# n = int(input("Enter a number: "))

# for i in range (1,n):
#     for j in range (1,n):
#         print(i*j,end =" ")
#     print()    

## Q - 5
for i in range (1,6):
    for j in range (1,i+1):
        
        print(j,end =" ")
    print()    

# Q - 6

for i in range (6,0,-1):
    for j in range (5,i-1,-1):
        print(j, end = " ")
        
    print()    

# ## Q - 7

for i in range (5,0,-1):
    
    for j in range (i,6):
        
        print(j, end = " ")
    print()   

# ## Q - 8

for i in range (1,6,1):
    
    for j in range (i,6):
       
        print(j, end = " ")
            
    print()
    