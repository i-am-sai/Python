from Python2.utils import Logger
from exceptions import LibraryError, BookNotFoundError, MemberNotFoundError, BookAlreadyCheckedOutError, BookNotCheckedOutError
from models import Book, Member
import json
from datetime import datetime
from utils import logger

class Library:
    def __init__(self):
        self.books = [] # stores all books
        self.members = [] # stores all members
        self.logger = Logger() # record library actions

        



    def add_book(self, book):
        self.books.append(book)
        logger.info(f"Book added: {book.title}")
        

    def save_book(self):
        # data = {
        #     "books": [book.to_dict() for book in self.books]
        # }
        book_list = []
        for book in self.books:
            book_list.append(book.to_dict())

        data = {
         "books": book_list
         }
        # filename = datetime.now().strftime("books_%Y%m%d_%H%M%S.json")
        with open("data/books.json", "w") as file:
                    json.dump(data, file, indent=4)

        # with open("data/books.json", "w") as file:
        #     json.dump(data, file, indent=4)


    
    def add_member(self, member):
        self.members.append(member)
        self.logger.info(f"Member added: {member.name}")
   
    
    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise BookNotFoundError(f"Book with ID {book_id} not found")

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise MemberNotFoundError(f"Member with ID {member_id} not found.")
    
    def checkout_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if book.is_checked_out:     # By default it will check for True if False then dont run it true then run
            raise BookAlreadyCheckedOutError(
                f"Book '{book.title}' is already checked out."
            )
        
        book.is_checked_out = True
        member.borrowed_books.append(book)
        self.logger.info(f"{member.name} checked out '{book.title}'.")

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if book not in member.borrowed_books:
            raise BookNotCheckedOutError(f"Book '{book.title}' was not checked out by {member.name}.")

        book.is_checked_out = False
        member.borrowed_books.remove(book)
        self.logger.info(f"{member.name} returned '{book.title}'.")

    
    def list_all_books(self):
        return self.books

    def list_all_members(self):
        return self.members

    #List Comprehension
    def list_checked_out_books(self):
        return [book for book in self.books if book.is_checked_out]

    #Same method withour list comprehension
    def list_check_out_books(self):
        checked_out_books = []

        for book in self.books:
            if book.is_checked_out:
                checked_out_books.append(book)

        return checked_out_books

    def find_book_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

