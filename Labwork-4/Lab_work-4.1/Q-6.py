def sum_and_product(*args):
    """Calculates both the sum and product of an arbitrary number of arguments."""
    if not args:
        return 0
        
    total = 0
    product = 1
    
    for num in args:
        total += num
        product *= num
        
    return total, product

s, p = sum_and_product(2,5,7,9)
print("Sum : ",s)
print("Product : ",p)
