# Q.5: Append a line to an existing file

with open("notes.txt","a") as f:
    f.write("Line 4:Python supports multiple modes of file handling.\n")
print("Appended successfully.")