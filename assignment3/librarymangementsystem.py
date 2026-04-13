# Custom Exception 
class BookNotAvailableError(Exception):
    """Raised when a user tries to borrow a book that is not available."""
    pass


# Book class 

class Book:
    """Represents a physical book in the library."""

    def __init__(self, book_id, title, author, is_available=True):
        self.__book_id      = book_id        # private
        self.__title        = title          # private
        self.__author       = author         # private
        self.__is_available = is_available   # private

    # read-only properties 
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def is_available(self):
        return self.__is_available

    # setter with validation 
    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_available must be True or False.")
        self.__is_available = value

    def get_details(self):
        status = "Available" if self.__is_available else "Not Available"
        return (f"ID: {self.__book_id} | Title: {self.__title} "
                f"| Author: {self.__author} | Status: {status}")

    def borrow_book(self):
        if not self.__is_available:
            raise BookNotAvailableError(f"'{self.__title}' is currently not available.")
        self.__is_available = False

    def return_book(self):
        self.__is_available = True


# EBook class (Inheritance) 

class EBook(Book):
    """
    Inherits from Book.
    Adds digital-specific attributes: file format and download URL.
    """

    def __init__(self, book_id, title, author, file_format, download_url, is_available=True):
        super().__init__(book_id, title, author, is_available)  # call parent constructor
        self.__file_format  = file_format    
        self.__download_url = download_url

    @property
    def file_format(self):
        return self.__file_format

    @property
    def download_url(self):
        return self.__download_url

    def get_details(self):                   # method overriding
        base = super().get_details()
        return f"{base} | Format: {self.__file_format} | URL: {self.__download_url}"


# User class 

class User:
    """Represents a library member."""

    def __init__(self, user_id, name):
        self.user_id        = user_id
        self.name           = name
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow_book()                   # raises BookNotAvailableError if unavailable
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False


# Library class 

class Library:
    """Manages books and users. Handles file storage."""

    def __init__(self):
        self.books = []
        self.users = []

    # search 
    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

    def search_user(self, name):
        for user in self.users:
            if name.lower() in user.name.lower():
                return user
        return None

    # borrow / return
    def borrow_book(self, user_name, book_title):
        user = self.search_user(user_name)
        book = self.search_book(book_title)
        if not user or not book:
            print("User or Book not found.")
            return
        try:
            user.borrow_book(book)
            print(f"'{user.name}' has borrowed '{book.title}'.")
        except BookNotAvailableError as e:
            print(f"Error: {e}")

    def return_book(self, user_name, book_title):
        user = self.search_user(user_name)
        book = self.search_book(book_title)
        if not user or not book:
            print("User or Book not found.")
            return
        if user.return_book(book):
            print(f"'{user.name}' has returned '{book.title}'.")
        else:
            print(f"'{user.name}' did not borrow '{book.title}'.")

    # display 
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\n--- All Books ---")
        for book in self.books:
            print(book.get_details())

    def display_users(self):
        if not self.users:
            print("No users registered.")
            return
        print("\n--- All Users ---")
        for user in self.users:
            borrowed = [b.title for b in user.borrowed_books]
            print(f"ID: {user.user_id} | Name: {user.name} | Borrowed: {borrowed}")

    # register user
    def register_user(self, user_id, name):
        if self.search_user(name):
            print(f"User '{name}' already exists.")
        else:
            self.users.append(User(user_id, name))
            print(f"User '{name}' registered successfully.")

    # file handling
    def load_books_from_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) != 4:
                        continue                  # skip malformed lines
                    book_id, title, author, is_available = parts
                    self.books.append(Book(book_id, title, author, is_available == "True"))
            print(f"Books loaded from '{file_path}'.")
        except FileNotFoundError:
            print(f"'{file_path}' not found. Starting with empty book list.")
        except ValueError as e:
            print(f"Error reading book file: {e}")

    def load_users_from_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) != 2:
                        continue
                    user_id, name = parts
                    self.users.append(User(user_id, name))
            print(f"Users loaded from '{file_path}'.")
        except FileNotFoundError:
            print(f"'{file_path}' not found. Starting with empty user list.")
        except ValueError as e:
            print(f"Error reading user file: {e}")

    def save_books_to_file(self, file_path):
        try:
            with open(file_path, "w") as f:
                for book in self.books:
                    f.write(f"{book.book_id},{book.title},{book.author},{book.is_available}\n")
            print(f"Books saved to '{file_path}'.")
        except OSError as e:
            print(f"Could not save books: {e}")

    def save_users_to_file(self, file_path):
        try:
            with open(file_path, "w") as f:
                for user in self.users:
                    f.write(f"{user.user_id},{user.name}\n")
            print(f"Users saved to '{file_path}'.")
        except OSError as e:
            print(f"Could not save users: {e}")


# Menu & Main 

def menu():
    print("\n========== Library Menu ==========")
    print("1. Display all books")
    print("2. Search a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Register a new user")
    print("6. Display all users")
    print("7. Exit")
    print("==================================")


def main():
    library = Library()
    library.load_books_from_file("books.txt")
    library.load_users_from_file("users.txt")

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.display_books()

        elif choice == "2":
            title = input("Enter book title to search: ").strip()
            book = library.search_book(title)
            if book:
                print(book.get_details())
            else:
                print("Book not found.")

        elif choice == "3":
            name  = input("Enter your name: ").strip()
            title = input("Enter book title: ").strip()
            library.borrow_book(name, title)

        elif choice == "4":
            name  = input("Enter your name: ").strip()
            title = input("Enter book title: ").strip()
            library.return_book(name, title)

        elif choice == "5":
            uid  = input("Enter user ID: ").strip()
            name = input("Enter user name: ").strip()
            library.register_user(uid, name)

        elif choice == "6":
            library.display_users()

        elif choice == "7":
            library.save_books_to_file("books.txt")
            library.save_users_to_file("users.txt")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()