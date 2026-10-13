# Q.7: Sort a Dictionary by Keys

grades = {"Zara": 85, "Alex": 92, "Charlie": 78, "Ben": 95}

sorted_by_keys = {key: grades[key] for key in sorted(grades)}

print("Dictionary Sorted by Keys : ")
print(sorted_by_keys)