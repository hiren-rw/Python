def separate(words_list):
    vowels_list = "aeiouAEIOU"
    starts_with_vowel = []
    starts_with_consonant = []
    
    for word in words_list:
        # Check if the word is not empty before checking its first letter
        if len(word) > 0:
            first_letter = word[0]
            
            if first_letter in vowels_list:
                starts_with_vowel.append(word)
            else:
                starts_with_consonant.append(word)
                
    return starts_with_vowel, starts_with_consonant

user_input = input("Enter a list of words separated by spaces : ")
all_words = user_input.split()

# Get the two separate lists back
vowel_words, consonant_words = separate(all_words)

print("Words starting with vowels :", vowel_words)
print("Words starting with consonants :", consonant_words)
