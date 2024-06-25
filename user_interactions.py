import time
import os
from classes import User
from classes import user_db, library_catalog, author_catalog
from classes import search_book_by_title, display_user, display_all_users, add_user, add_book, display_all_books,display_all_users,view_author,view_all_authors, add_new_author

current_user = User("King James",99999)

def clear():
    os.system('cls')

def main():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit           
                    
Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            book_ops()
            time.sleep(6)
            clear()
        elif ans == '2':
            user_ops()
            time.sleep(6)
            clear()
        elif ans == '3':
            author_ops()
            time.sleep(6)
            clear()
        elif ans == '4':
            print("Thanks for using the Library Management System!")
            break
        else:
            print("Invalid data entry. Try again")

def book_ops():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
Book Operations:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    6. Main Menu
                    
Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date: ")
            add_book(library_catalog, author_catalog, title, author_name, genre, publication_date)
            time.sleep(8)
            clear()
        elif ans == '2':
            title = input("Enter the title of the book you'd like to borrow: ")
            current_user.borrow_book(title)
            time.sleep(6)
        elif ans == '3':
            title = input("INput the book you are returning:")
            current_user.return_book(title)
            time.sleep(6)
        elif ans == '4':
            title = input("Enter the title of the book you'd like to search for: ")
            search_book_by_title(library_catalog, title)
            time.sleep(6)
            clear()
        elif ans == '5':
            display_all_books()
            time.sleep(6)
            clear()
        elif ans == '6':
            main()
            time.sleep(6)
            clear()
        else:
            print("Invalid data entry. Try again")


def user_ops():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
User Operations:
    1. Add a new user
    2. View user details
    3. Display all users
    4. Main Menu         
                    
Enter the corresponding number for the action you'd like to take here: """)

        if ans == '1':
            name = input("Please enter your name: ")
            print(f"This is the entered name: {name}")
            correct = input("Please confirm the name listed above is correct: y/n")
            if correct.lower() == 'y':
                add_user(name)
                time.sleep(6)
                clear()
        elif ans == '2':
            library_id = int(input("Enter the library_id of the user you'd like to search for: "))
            display_user(library_id)           
            time.sleep(6)
            clear()
        elif ans == '3':
            display_all_users()
            time.sleep(6)
            clear()
        elif ans == '4':
            main()
            time.sleep(6)
            clear()
        else:
            print("Invalid data entry. Try again")

def author_ops():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
    Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Main Menu         
                    
Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            author_name = input("Enter the author you'd like to add: ")
            author_bio = input("Input the biography for the author")
            add_new_author( author_name, author_bio)
            time.sleep(6)
            clear()
        elif ans == '2':
            author_name = input("Enter the author name you'd like to view: ")
            view_author(author_catalog, author_name)
            time.sleep(6)
            clear()
        elif ans == '3':
            view_all_authors()
            time.sleep(6)
            clear()
        elif ans == '4':
            main()
            time.sleep(6)
            clear()
        else:
            print("Invalid data entry. Try again")

main()
