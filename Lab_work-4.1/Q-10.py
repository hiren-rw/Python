def cost(**kwargs):
    """
    Expects keyword arguments for product values. 
    Requires 'price' and 'quantity' to compute the total cost.
    """
    product_name = kwargs.get('name', 'Unknown Item')
    price = kwargs.get('price', 0.0)
    quantity = kwargs.get('quantity', 0)
    
    total_cost = price * quantity
    return f"Product: {product_name} | Total Cost: ${total_cost:.2f}"

invoice = cost(name="Laptop", price=899.99, quantity=3)
print(invoice)
