username = "Default_User"
print("Starting username :", username)

def change_name(new_name):
    global username  # Target the global variable
    username = new_name

new_name = input("Enter a new username : ")
change_name(new_name)

print("The updated global username is :", username)
