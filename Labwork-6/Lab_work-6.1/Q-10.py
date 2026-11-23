# Q.10: Copy content line by line

with open("source.txt","r") as f1:
    data = f1.read()
    print("Content copied from source file.")

with open("backup.txt","w") as f2:
    f2.write(data)
    print("Content Written in backup file Successfully!")