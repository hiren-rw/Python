class Book:
    def __init__(self):
        self.__title = ""   # Private attribute
        self.__author = ""  # Private attribute

    # Public setter methods
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # Public getter methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

# Testing the Book class
my_book = Book()
my_book.set_title("1984")
my_book.set_author("George Orwell")

print("Book Title: ",my_book.get_title())
print("Author: ",my_book.get_author())