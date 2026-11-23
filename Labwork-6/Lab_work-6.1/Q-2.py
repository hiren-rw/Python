# Q.2: Read content, then overwrite it

with open("sample.txt","r") as file:
    print("Reading Existing Content : ")
    print(file.read())

with open("sample.txt","w") as file:
    file.write("Learning file handling in Python is fun!")

print("New Content Overwritten successfully...")