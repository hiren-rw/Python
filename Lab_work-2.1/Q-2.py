age = int(input("Enter your Age : "))

if age<=12:
    print("You are Child.")
else:
    if age<=19:
        print("You are Teenager.")
    else:
        if age<=59:
            print("You are Adult.")
        else:
            print("You are Senior.")
