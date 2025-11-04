'''Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message'''

for i in range(1,5):
    print("You Travelled: ",i,"km")
    result = input("are you tired?:")
    if result == "yes":
        print("you didn't finish the race")
        break
    else:
        if i==4:
            print("You successfully Completed 5 Km.\n Congratulations!")
            break
        continue

