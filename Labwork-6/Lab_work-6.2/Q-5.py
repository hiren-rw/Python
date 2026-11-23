# Q.5: File Handling with finally Block

file = None
try:
    file = open("sample2.txt", "r")
    print(file.read())
    
except FileNotFoundError:
    print("Error: File does not exist.")
finally:
    if file is not None:
        file.close()
        print("File closed.")