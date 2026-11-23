# Q.4: check_palindrome(s) asserting string is not empty

def check_palindrome(s):
    assert len(s)>0,"String cannot be Empty!"

    if s == s[::-1]:
        print("It is a palindrome.")
    else:
        print("Not a palindrome.")

s = input("Enter a string : ")
check_palindrome(s)