count = 0

def my_function():
    global count        # Global Keyword
    count = count + 1
    print("Function has been executed! -",count)

# Ask the user how many times to call the function
loops = int(input("How many times do you want to run the function? : "))

for i in range(loops):
    my_function()

print("Total number of times the function was called :",count)
