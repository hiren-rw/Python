# Q.4: String Index Out of Range with else Block

try:
    s1 = "Hello World!"
    i = int(input("Enter a Index Number : "))
    print(f"Value at Index {i} is '{s1[i]}'")

except IndexError:
    print("This Index is out of Range!")