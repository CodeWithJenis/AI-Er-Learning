india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city:")
if city in india:
    print("India")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("Bangladesh")
else:
    print("Not Found")

city1 = input("Enter a city:")
city2 = input("Enter a city:")

if(city1 in india and city2 in india):
    print("Both are from india")
elif(city1 in pakistan and city2 in pakistan):
    print("Both are from Pakistan")
elif(city1 in bangladesh and city2 in bangladesh):
    print("Both are from Bangladesh")
else:
    print("City 1 & City 2 are from two different country")
