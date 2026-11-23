# Q.3: Read and print contents line by line

with open("sample.txt","r") as file:
    for i in file:
        print(i,end="")