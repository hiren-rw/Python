# Q.8: Open a text file in read-write mode

with open("notes.txt","r+") as f:
    print("\nReading Existing content : \n")
    print(f.read())
    f.write("\nThis file was last modified by adding this sentence.")

    print("\nAppend Successfully.")