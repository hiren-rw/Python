a = float(input("Enter First Number : "))
b = float(input("Enter Second Number : "))
op = input("Enter any one Operator (+,-,*,/) : ")

match op:
    case '+':
        print("\nAddition is : ",a+b)
    
    case '-':
        print("\nSubtraction is : ",a-b)

    case '*':
        print("\nMultiplication is : ",a*b)
        
    case '/':
        print("\nDivision is : ",a/b)

    case _:
        print("\nInvalid Choice.")
