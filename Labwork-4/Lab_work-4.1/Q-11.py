def data(**kwargs):
    """Validates if essential fields exist in the employee attributes profile."""
    required_fields = ["name", "department", "salary"]
    missing_fields = []
    
    for field in required_fields:
        if field not in kwargs:
            missing_fields.append(field)
            
    if missing_fields:
        print(f"Warning! Missing mandatory fields: {', '.join(missing_fields)}")
    else:
        print(f"Employee {kwargs['name']} verified successfully for the {kwargs['department']} department.")

# Example usage:
data(name="John Doe", department="HR")  # Missing salary
data(name="Jane Smith", department="IT", salary=75000)
