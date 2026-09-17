print("--- Telecom Customer Support ---")
print("1. English\n2. Hindi\n3. Gujarati")
ch = input("Select your language : ")

match ch:
    case "1":
        print("\nEnglish Menu:\n1. Prepaid Services\n2. Postpaid Services\n3. Speak to an Executive")
        sub_choice = input("Select an option: ")
        match sub_choice:
            case "1": print("Redirecting to English Prepaid Services...")
            case "2": print("Redirecting to English Postpaid Services...")
            case "3": print("Connecting you to a customer care executive...")
            case _: print("Invalid entry.")
            
    case "2":
        print("\nHindi Menu:\n1. Prepaid Services\n2. Postpaid Services\n3. Speak to an Executive")
        sub_choice = input("Option chunein: ")
        match sub_choice:
            case "1": print("Hindi Prepaid sevaon ke liye redirect kiya ja raha hai...")
            case "2": print("Hindi Postpaid sevaon ke liye redirect kiya ja raha hai...")
            case "3": print("Kripya prateeksha karein, executive se connect kiya ja raha hai...")
            case _: print("Amanuya vikalp.")
            
    case "3":
        print("\nGujarati Menu:\n1. Prepaid Services\n2. Postpaid Services\n3. Speak to an Executive")
        sub_choice = input("Option pasand karo: ")
        match sub_choice:
            case "1": print("Gujarati Prepaid sevao mate redirect thai rahyu che...")
            case "2": print("Gujarati Postpaid sevao mate redirect thai rahyu che...")
            case "3": print("Krupa kari raah juo, executive sathe jodan thai rahyu che...")
            case _: print("Amanuya vikalp.")
            
    case _:
        print("Invalid language selection.")
