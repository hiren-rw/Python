def frequency(text):
    
    frequency_dict = {}
    
    for i in text:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1
            
    return frequency_dict

text = input("Enter any string : ")
result = frequency(text)

print("Original Text : ",text)
print("Character Frequencies : ",result)
