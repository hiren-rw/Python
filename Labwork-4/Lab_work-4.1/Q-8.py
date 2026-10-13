def filter(*args):
    # Filter strings and numbers using list comprehensions
    strings = tuple(item for item in args if isinstance(item, str))
    numbers = tuple(item for item in args if isinstance(item, (int, float)) and not isinstance(item, bool))
    
    return strings, numbers


strings, numbers = filter("apple", 10, 3.14, "banana", 42)
print("Strings :", strings)
print("Numbers :", numbers)
