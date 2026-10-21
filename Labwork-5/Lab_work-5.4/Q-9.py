# Q.9: Overloading with Flexible Arguments (*args)

class Printer:
    def print_data(self, *args):
        if len(args) == 1:
            # __name__ is used for displaying only name.
            print(f"Single item received : {args[0]} (Type: {type(args[0]).__name__})")
        elif len(args) == 2:
            print(f"Two items received : {args[0]} and {args[1]}")
        else:
            print("Invalid number of arguments.")

p = Printer()

p.print_data("Hello")
p.print_data(100)
p.print_data("Score", 95)