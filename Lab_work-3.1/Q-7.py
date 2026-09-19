text = "Hello World"
print("Starts with 'Hello' :", text.startswith("Hello"))
print("Ends with 'World' :", text.endswith("World"))

mixed_str = "Data123#Science!"
clean_str = ""
for char in mixed_str:
    if char.isalpha():
        clean_str += char
print("Cleaned string :", clean_str)

print("Reversed :", "Python"[::-1])
