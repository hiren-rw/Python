# Q.9: Search for a word and display its line number(s)

word = input("Enter any word for searching : ")
line_number = 1
found = False

with open("sample.txt","r") as file:

    for line in file:
        if word in line:
            print(f"Word '{word}' founded at line : {line_number}")
            found = True
        
        line_number += 1

    if not found:
        print("Word not found!")