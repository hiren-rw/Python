def get_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    
    return square, cube

num = float(input("Enter a number : "))

result = get_square_and_cube(num)

print("Resulting tuple (Square, Cube) :", result)
