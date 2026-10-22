from library import Library
from models import Book, Member
from exceptions import LibraryError, OptionNotFoundError, BookNotFoundError, MemberNotFoundError, BookAlreadyCheckedOutError, BookNotCheckedOutError
from utils import logger

library = Library()

book1 = Book(1, "Why I am an Athiest", "Bhagath Singh")
book2 = Book(2, "Sapiens", "Yuval Nova Harari")

member1 = Member(1, "Sai" )
member2 = Member(2, "Swaroop")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

library.checkout_book(1, 1)

def display_menu():
    print("********************************************************************************")
    print("\n Welcome to our Terminal Library: Please Select a option below to proceed \n")
    print("option 1: Donate book to Library")
    print("option 2: register member to Library")
    print("option 3: check Available books in Library")
    print("option 4: check registered member in Library")
    print("option 5: checkout and rent a book of you choice")
    print("option 6: return book to library")
    print("option 7: Exit from Library portal \n")

while True:
  display_menu()
  
  user_input = input("Enter option of your choice: ")

  try:
     option_entered = int(user_input)   
  except ValueError:
     print(f" '{user_input} is not a valid option number. Please enter a number")
     continue

  if option_entered == 1:
     book_id = int(input("Enter Book ID: "))
     book_name = input("Enter Book Name: ")
     author_name = input("Enter Author Name: ")
     library.add_book(Book(book_id, book_name, author_name))
     library.save_book()
     print(f"Succesfully added {book_id}")
     logger.info(f"Added Book {book_id}")

  elif option_entered == 2:
     member_id = int(input("Enter Memeber ID"))
     member_name = input("Enter Member name")  
     library.add_member(Member(member_id, member_name))
     print(f"Succesfully added {member_id}")   

  elif option_entered == 3:
     print(library.list_all_books())

  elif option_entered == 4:
     print(library.list_all_members())

  elif option_entered == 5:
     try:
        b_id = int(input("Enter book id to checkout: "))
        m_id = int(input("Enter member id to checkout: "))
        library.checkout_book(m_id, b_id)
        print("Checkout successfull")
     except LibraryError as e:
        print(f"could not checkout: {e}") 
     

  elif option_entered == 6:
      try:
         b_id = int(input("Enter book id to return : "))
         m_id = int(input("Enter member id to return : "))
         library.return_book(m_id, b_id)
         print("Return successfull")
      except LibraryError as e:
         print(f"could not return: {e}")
      
  elif option_entered == 7:
    print("Exiting from Library Portal, Thank You!")
    break                  

  else:
     raise OptionNotFoundError(f" Option {option_entered} is not a valid menu choice.")


# print(library.list_all_books())
# print(library.list_all_members())
# try:
#     library.checkout_book(43, 43)
# except LibraryError as e:
#     print(f"Handled error: {type(e).__name__} - {e}")

# try:
#     library.checkout_book(43, 43)
# except LibraryError as e:
#     print(f"Edge Case")