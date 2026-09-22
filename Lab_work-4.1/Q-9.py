def print_person_info(**kwargs):
    """Prints key-value pairs representing a person's profile information."""
    print("--- Person Profile ---")
    for key, value in kwargs.items():
        # Title case the key for neat formatting (e.g., 'birth_place' -> 'Birth_place')
        print(f"{key.title()}: {value}")


print_person_info(name="Sarah", age=28, city="New York", occupation="Engineer")
