def rectangle(length, width):
    
    area = length * width
    perimeter = 2 * (length + width)
    
    return area, perimeter

# Take length and width input from the user
length = float(input("Enter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))

rect_area, rect_perimeter = rectangle(length,width)

print("Area of Rectangle :", rect_area)
print("Perimeter of Rectangle :", rect_perimeter)
