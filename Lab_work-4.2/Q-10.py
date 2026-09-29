total = 0

def add_to_total(number):
    global total  # Tell Python we are changing the global variable
    total = total+number

inputs = int(input("How many numbers do you want to enter? :"))

for i in range(inputs):
    user_num = float(input(f"Enter number {i + 1} : "))
    add_to_total(user_num)
    print("Current running total sum :", total)

print("Final total sum of all numbers entered :", total)
