# First, a simple function to check if a single number is prime
def is_prime(num, divisor=2):
    if num <= 1:
        return False
    if divisor == num:
        return True
    if num % divisor == 0:
        return False
    # Check the next number
    return is_prime(num, divisor + 1)

# Second, the function to loop through your start and end points
def print_primes(start, end):
    # Stop when the start number goes past the end number
    if start > end:
        return
    
    # If the current number is prime, print it
    if is_prime(start):
        print(start, end=" ")
        
    # Move to the next number
    print_primes(start + 1, end)

a = int(input("Enter Start Number : "))
b = int(input("Enter End Number : "))
print(f"Prime Numbers Between {a} and {b} : ")
print_primes(a,b)
