num = list(map(int,(input("Enter Numbers seperated by spaces : ").split())))
print("List : ",num)

odd = list(filter(lambda i: i%2!=0,num))
print("Odd Numbers : ",odd)
