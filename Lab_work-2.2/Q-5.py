print("--- Fast-Food Menu ---")
print("1. Sandwich\n2. Pizza\n3. Burger")
ch = input("Enter Your Choice : ")

match ch:
    case "1":
        print("\nTypes of Sandwich : \n1. Veg Grilled \n2. Cheese Corn")
        sub_choice = input("Choose your sandwich subtype: ")
        match sub_choice:
            case "1": print("Ordered: Veg Grilled Sandwich")
            case "2": print("Ordered: Cheese Corn Sandwich")
            case _: print("Invalid subtype selection.")
            
    case "2":
        print("\nTypes of Pizza:\n1. Thin Crust\n2. Cheese Burst\n3. Fresh Dough")
        sub_choice = input("Choose your pizza subtype: ")
        match sub_choice:
            case "1": print("Ordered: Thin Crust Pizza")
            case "2": print("Ordered: Cheese Burst Pizza")
            case "3": print("Ordered: Fresh Dough Pizza")
            case _: print("Invalid subtype selection.")
            
    case "3":
        print("\nTypes of Burger:\n1. Aloo Tikki\n2. Chicken Zinger")
        sub_choice = input("Choose your burger subtype: ")
        match sub_choice:
            case "1": print("Ordered: Aloo Tikki Burger")
            case "2": print("Ordered: Chicken Zinger Burger")
            case _: print("Invalid subtype selection.")
            
    case _:
        print("Invalid selection.")
