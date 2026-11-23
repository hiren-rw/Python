# Q.6: Open a file in binary mode

with open("notes.txt","rb") as f:
    print("Reading file in Binary : ")
    print(f.read())