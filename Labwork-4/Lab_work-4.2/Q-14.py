def calculate_stats(numbers_list):
    
    total = sum(numbers_list)
    highest = max(numbers_list)
    lowest = min(numbers_list)
    
    return total, highest, lowest

input_string = input("Enter a series of integers separated by spaces : ")
user_numbers = [int(n) for n in input_string.split()]

# Unpack the three returned values into three separate variables
total_sum, max_val, min_val = calculate_stats(user_numbers)

print("Your numbers list :", user_numbers)
print("Sum total of items :", total_sum)
print("Maximum value in list :", max_val)
print("Minimum value in list :", min_val)
