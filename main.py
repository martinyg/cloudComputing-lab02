import os
from collections import Counter
import socket



#a.	[DONE]List name of all the text file at location: /home/data
#b.	[DONE]Read the two text files and count total number of words in each text files
#c.	[DONE]Add all the number of words to find the grand total (total number of words in both files)
#d.	[DONE]List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
#e.	[DONE]Find the IP address of your machine
#f.	Write all the output to a text file at location: /home/output/result.txt (inside your container).
#g.	Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

print("Hello World \nHere are the files in the directory:")

dirFiles = os.listdir('data/')

for file in dirFiles:
    print(file)

f1 = open("data/IF.txt", "r")
f2 = open("data/Limerick.txt","r")


print("\nHere are the total number of words in: IF.txt")
f1words = 0
f1lines = f1.read()
f1data = f1lines.split()
f1words += len(f1lines)
print(f1words)

print("\nHere are the 3 most common words in IF.txt")

with open("data/IF.txt") as f1:
    words = [word for line in f1 for word in line.split()]
    c = Counter(words)
    i = 0
    for word, count in c.most_common():
        print(word, count)
        i += 1
        if i == 3:
            break

print("\nHere are the total number of words in: Limerick.txt")
f2words = 0
f2lines = f2.read()
f2data = f2lines.split()
f2words += len(f2lines)

print(f2words)

print("\nThe total number of words in both files is:")
print(f1words + f2words)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("\nYour Machine's IP Address = " + IPAddr)

