# Q.8: Sort a Dictionary by Values

prices = {"Laptop": 1200, "Mouse": 25, "Monitor": 300, "Keyboard": 75}

sorted_by_values = dict(sorted(prices.items(), key=lambda item: item[1]))

print("Dictionary Sorted by Values : ")
print(sorted_by_values)