# Q.2: check_even() with TypeError and ValueError

def check_even(n):
    if type(n) != int:
        raise TypeError("Value is not Integer!")
    elif n%2 != 0:
        raise ValueError("Number is Odd!")
    else:
        print(f"Number {n} is Even.")

check_even(20)
# check_even(0.4)     # Raises TypeError
check_even(51)      # Raises ValueError