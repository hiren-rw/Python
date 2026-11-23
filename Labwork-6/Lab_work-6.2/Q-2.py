# Q.2: List Index Out of Range

try:
    l1 = [10,44,52,39,99]
    i = int(input("Enter a Index Number : "))
    print(f"Value at Index {i} is {l1[i]}")

except IndexError:
    print("This Index is out of Range!")