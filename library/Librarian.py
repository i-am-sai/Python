from library import Library
from models import Book, Member
from exceptions import LibraryError, OptionNotFoundError, BookNotFoundError, MemberNotFoundError, BookAlreadyCheckedOutError, BookNotCheckedOutError

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
    print("Welcome to our Terminal Library: Please Select a option below to proceed")
    print("option 1: Donate book to Library")
    print("option 2: register member to Library")
    print("option 3: check Available books in Library")
    print("option 4: check registered member in Library")
    print("option 5: checkout and rent a book of you choice")
    print("option 6: return book to library")
    print("option 7: Exit from Library portal")



while True:
  display_menu()
  
  
  user_input = input("Enter option of your choice: -")
  option_entered = int(user_input)   

  if option_entered == 1:
     book_id = input("Enter Book ID: ")
     book_name = input("Enter Book Name: ")
     author_name = input("Enter Author Name: ")
     library.add_book(Book(book_id, book_name, author_name))
     print(f"Succesfully added {book_id}")
     break

  if option_entered == 2:
     member_id = input("Enter Memeber ID")
     member_name = input("Enter Member name")  
     print(f"Succesfully added {member_id}")     

  elif option_entered == 3:
     print(library.list_all_books())
     break

  elif option_entered == 4:
     print(library.list_all_members())
     break

  elif option_entered == 5:
     b_id = input("Enter book id to checkout: ")
     m_id = input("Enter member id to checkout: ")
     library.checkout_book(m_id, b_id)
     print("Checkout successfull")
     break
     
     
  elif option_entered == 7:
    print("Exiting from Library Portal, Thank You!")
    break                  

print(library.list_all_books())

# while True:
#   display_menu()
#   option_list = [1,2,3,4,5,6]
  
#   user_input = input("Enter option of your choice: -")
#   option_entered = int(user_input)
#   try: 
#     for option in option_list:
#         if option == option_entered:
            

#             if option_entered == 6:
#                         print("Exiting from Library Portal, Thank You!")
#                         break

#   except OptionNotFoundError as e:
#      print(f"Handled error: {e}")
     




    

   
     

  