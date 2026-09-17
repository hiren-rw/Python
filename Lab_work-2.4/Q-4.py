n = int(input("Enter a number N: "))

for i in range(1,n+1):
    print("Multiplication Table of",i,":")
    
    for j in range(1, 11):
        print(i,"X",j,"=",i*j)
    print()
