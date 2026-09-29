def sum_digits(num):
    # Base Case: If the number is already a single digit, just return it
    if num < 10:
        return num
    
    # Take the last digit and add it to the rest of the numbers
    last_digit = num % 10
    remaining_digits = num // 10
    
    # Add them together and send it back into the function to check again
    total = last_digit + sum_digits(remaining_digits)
    
    # If the final sum is still 10 or bigger, run the function again
    return sum_digits(total)

# Test the program
n = int(input("Enter Number : "))
print("Sum of Digits : ",sum_digits(n))  
# How it works: 9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2. Output: 2
