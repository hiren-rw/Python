global_input = input("Enter value for the GLOBAL variable : ")
x = global_input

def show_scopes():
    # Take input to set up a completely separate local variable with the same name
    local_input = input("Enter value for the LOCAL variable (inside function) : ")
    x = local_input
    print("Value inside the function (local x) :", x)

show_scopes()
print("Value outside the function (global x) :", x)
