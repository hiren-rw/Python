# Q.4: Write multiple lines to a file

with open("notes.txt","w") as file:
    file.write("Line 1:Python is easy to learn.\nLine 2:It has numerous libraries.\nLine 3:File handling is one of its features.\n")
print("Written successfully.")