x=input("Enter 1st number: ")
y=input("Enter 2nd number: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    z = None
    print(e)
print(z)