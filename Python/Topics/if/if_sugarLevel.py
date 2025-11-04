sugarLevel = input("Please enter your sugar level: ")
sugarLevel = int(sugarLevel)
if (sugarLevel<80):
    print("The sugar level is low")
elif (sugarLevel>100):
    print("The sugar level is high")
else:
    print("The sugar level is normal")