def cube(x):
    """Helper function to calculate the cube of a number."""
    return x ** 3

def process_list(func, numbers):
    """UDF that accepts another function and a list of numbers as arguments."""
    return [func(num) for num in numbers]

# Example usage:
nums = [1, 2, 3, 4,5]
result = process_list(cube, nums)
print("Original List : ",nums)
print("Cubes of the list : ",result)
