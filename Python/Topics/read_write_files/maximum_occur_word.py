'''
poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your
python program and find out words with maximum occurance.
'''

word_stats={}

with open("D:\\Carrer\\AI\\Python Learning\\first_python\\read_write_files\\poem.txt.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)