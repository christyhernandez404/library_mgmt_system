class Book:
    def __init__(self, title, author, genre, publication_date, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = availability_status

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Date: {self.publication_date}")
        print(f"Avalability: {self.availability_status}")

    # getter
    def get_availability(self):
        return self.availability_status

    # setter
    def set_availability(self, status):
        # why is it status in Available and Not available? where do i change the status if it's not in the setter
        if status in ["Available", "Not Available"]:
            self.availability_status = status
        else:
            print("Invalid status. Please set status to 'Available' or 'Not Available'.")


def add_book(library_catalog, author_catalog, title, author_name, genre, publication_date):
    if author_name not in author_catalog:
        author_biography = "This author is new. Biography will be added at a later time."
        new_author = Author(author_name, author_biography)
        author_catalog[author_name] = new_author
        print(f"{author_name} has been added to the author catalog.")

        author_instance = author_catalog[author_name]
        new_book = Book(title, author_instance, genre,
                        publication_date, availability_status='Available')
        new_library_id = max(library_catalog.keys()) + 1
        library_catalog[new_library_id] = new_book
        print(f"You've added '{title}' by {
              new_book.author.name} to the library management system!")


def search_book_by_title(library_catalog, title):
    found = False
    for book in library_catalog.values():
        if book.title.lower() == title.lower():
            book.display_info()
            found = True
    if not found:
        print("The book title you name is not in our library catalog")


def display_all_books():
    print("All books in our library catalog:")
    for book_id, book_instance in library_catalog.items():
        book_instance.display_info()


library_catalog = {
    1: Book("Game of Thrones", "George R Martin", "Fantasy", "1996", "Available"),
    2: Book("All About Love", "Bell Hooks", "Non Fiction", "2018", "Available")
}  # library_catalog needs to have instances of Book

# ===================================================================================================


class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    # getter for library_id
    def get_library_id(self):
        return self.library_id

    # setter for library_id
    def set_library_id(self, library_id):  # need to pass in a libary id to update
        self.library_id = library_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.library_id}")

    def borrow_book(self, book):
        if book.availability_status == "Available":
            book.availability_status = "Borrowed"
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {
                book.title} and its status in the library catalog is now{book.availability_status}!")
        else:
            print("Book is unavailable right now. Please come by later")

def display_user(library_id):
    for user in user_db.values():
        if user.get_library_id() == library_id:
            user.display_info()
            break
        else:
            print("user not found. please re-enter a library id")

def add_user(name):  # this function will  create an instance of the user class
    new_user_id = max(user_db.keys()) + 1
    # for loop used to find max library_id in user db because it's not the key?
    new_library_id = max(user.library_id for user in user_db.values()) + 1
    new_user = User(name, new_library_id)
    user_db[new_user_id] = new_user
    print(f"{name} has been added to our library mgmt system! Please save your library id {
          new_library_id}.")



def return_book(self, book):
    if book in self.borrowed_books:
        self.borrowed_books.remove(book)
        book.availability_status = "Available"
        print(f"{self.name} has returned {
            book.title} and its status in the library catalog is now {book.availability_status}!")
    else:
        print(f"{self.name} does not have this {book.title}")



    

# adding a user to the database #why does this need to exist outside of the User class?
# displaying all users


def display_all_users():
    print("Below are all the users of the library mgmt system:")
    for user in user_db.values():
        user.display_info()


user_db = {
    1: User("Christy", 12345),
    2: User("Hiro", 12346)}


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Biography: {self.biography}")


def add_new_author(author_name, author_bio):
    new_author_id = max(author_catalog.keys()) + 1
    new_author = Author(author_name, author_bio)
    author_catalog[new_author_id] = new_author
    print(f"{author_name} has been added to the author catalog!")


def view_all_authors():
    print("Below are all the authors the library mgmt system has:")
    for author in author_catalog.values():
        author.display_info()


def view_author(author_catalog, author_name):
    found = False
    for author in author_catalog.values():
        if author.name.lower() == author_name.lower():
            author.display_info()
            found = True
    if not found:
        print("Unfortunately the author you entered is not in the author catalog.")


author_catalog = {
    1: Author("George R Martin", "Biography for George R Martin"),
    2: Author("Bell Hooks", "Biography for Bell Hooks")}




