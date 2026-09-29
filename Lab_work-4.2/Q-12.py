def initialize_variable():
    global counter
    counter = 0  # Create and set the variable to 0
    print("Counter initialized to:", counter)

def increment(amount):
    global counter
    counter = counter + amount  # Add the user's value to the global variable

# Call the first function to initialize the variable
initialize_variable()

# Ask the user for a value to add to the counter
value = float(input("Enter a value to add to the counter : "))
increment(value)

print("Final counter value after incrementing :", counter)
