'''We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
Solution
'''

# But best will be done through function

country_population = {"china": 143, "india": 136,"usa": 32, "pakistan": 21}
user_input = input("Enter any three type of inputs: 1) 'print', 2)'add', 3) 'remove' : ")
if user_input == "print":
    for k,v in country_population.items():
        print(f"{k}==>{v}")
elif user_input == "add":
    country = input("Enter country name: ")
    if country in country_population.keys():
        print(f"{country} already exits")
    else:
        population = input("Enter country population: ")
        population = int(population)
        country_population[country] = population
        for key in country_population:
            print(f"{key}==>{country_population[key]}")
else:
    country = input("Enter country name: ")
    if country in country_population.keys():
        del country_population[country]
        for k, v in country_population.items():
            print(f"{k}==>{v}")
    else:
        print("Country not found")
country = input("Which country you want to query?")
if country in country_population.keys():
    print(f"Country Population = {country_population[country]}")
else:
    print("Country not found")