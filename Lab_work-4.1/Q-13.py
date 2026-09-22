def fibonacci(n):
    """
    Working:
        Generates the Fibonacci sequence up to a maximum value of 'n'.
        The sequence starts with 0 and 1, and each subsequent number is 
        the sum of the two preceding numbers (0, 1, 1, 2, 3, 5, 8, ...).
        The loop terminates as soon as the next number exceeds 'n'.

    Input:
        n (int): The upper limit numerical value for the sequence.

    Output:
        list: A list of integers containing the Fibonacci sequence up to 'n'.
    """
    if n < 0:
        return []
        
    sequence = [0]
    if n == 0:
        return sequence
        
    sequence.append(1)
    
    # Generate subsequent numbers until the value exceeds n
    while True:
        next_num = sequence[-1] + sequence[-2]
        if next_num > n:
            break
        sequence.append(next_num)
        
    return sequence

# Task 1: Print the docstring to fulfill the requirement
print("--- Function Documentation (Docstring) ---")
print(fibonacci.__doc__)

# Task 2: Example execution
limit = 20
result = fibonacci(limit)
print(f"Fibonacci sequence up to {limit}: {result}")
