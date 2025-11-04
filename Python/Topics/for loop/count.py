''' After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads '''

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
head_count=0
for i in result:
    if i == "heads":
        head_count = head_count + 1
print(head_count)
