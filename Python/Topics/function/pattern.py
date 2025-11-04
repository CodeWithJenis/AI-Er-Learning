''' Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops) '''

def print_pattern(number):
    for i in range(1,number+1):
        for j in range(i):
            print("*",end="")
        print(end="\n")
    return
print_pattern(0)



