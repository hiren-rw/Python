def split_vowels_and_others(text):
    vowels_list = "aeiouAEIOU"
    vowels = ""
    others = ""
    
    # Loop through each letter in the text
    for char in text:
        if char in vowels_list:
            vowels = vowels + char
        else:
            others = others + char
            
    return vowels, others

user_string = input("Enter any string/sentence : ")

# Unpacking
vowels, remaining = split_vowels_and_others(user_string)

print("Vowels :", vowels)
print("Remaining characters :", remaining)
