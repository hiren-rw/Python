def rectangle_area(length, width):
    """
    Purpose: Calculates and returns the area of a rectangle.
    Parameters:
        length (float/int): The long side dimension of the rectangle.
        width (float/int): The short side dimension of the rectangle.
    Return Type: 
        float/int: Total calculated surface area.
    """
    return length * width

# Task 1: Print the docstring
print("--- Function Documentation (Docstring) ---")
print(rectangle_area.__doc__)

# Task 2: Call the function normally
area = rectangle_area(5, 10)
print(f"Calculated Area: {area}")
