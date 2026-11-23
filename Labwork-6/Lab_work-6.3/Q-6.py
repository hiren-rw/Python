# Q.6: Custom InvalidEmailError in validate_email(email)

class InvalidEmailEoor(Exception):
    pass

def validate_email(email):
    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailEoor("Invalid Email Address!")
    
    print("Your Email is : ",email)

email = input("Enter Your Email : ")
validate_email(email)