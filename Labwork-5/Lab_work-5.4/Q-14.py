# Q.14: Initializing Parent Attributes using super()

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        print(f"User account created for : {self.username}")

class Admin(User):
    def __init__(self, username, email, access_level):
        # Initialize username and email using the User class constructor
        super().__init__(username, email)
        self.access_level = access_level
        print(f"Admin privileges granted with access level : {self.access_level}")

# Creating an Admin object
admin_user = Admin("Admin123", "admin@example.com", "Full Root Access")