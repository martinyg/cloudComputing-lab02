
#a.	List name of all the text file at location: /home/data
#b.	Read the two text files and count total number of words in each text files
#c.	Add all the number of words to find the grand total (total number of words in both files)
#d.	List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
#e.	Find the IP address of your machine
#f.	Write all the output to a text file at location: /home/output/result.txt (inside your container).
#g.	Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

print("Hello World")


f2 = open("/data/Limerick.txt","r")
f1 = open("/data/IF.txt", "r")

