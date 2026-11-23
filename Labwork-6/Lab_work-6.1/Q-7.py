# Q.7: Count words, characters, and lines from a text file

lines = 0
words = 0
chars = 0

with open("notes.txt","r") as file:
    for i in file:
        lines += 1
        words += len(i.split())     # split will break words from line and len will count it.
        chars += len(i)

print("Total Lines : ",lines)
print("Total Words : ",words)
print("Total Charcters : ",chars)