from library import Library
from models import Book, Member
from exceptions import LibraryError, BookNotFoundError, MemberNotFoundError, BookAlreadyCheckedOutError, BookNotCheckedOutError


library = Library()

book1 = Book(1, "I am an Athiest", "Bhagath Singh")
book2 = Book(2, "Sapiens", "Yuval Nova Harari")

member1 = Member(1, "Sai" )
member2 = Member(2, "Swaroop")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

library.checkout_book(1,1)

try: 
    library.checkout_book(1,1)
except BookAlreadyCheckedOutError as e:
    print(f"Handled error: {e}")

print("Script continued")
print(library.list_checked_out_books())

try: 
    library.checkout_book(2,100)
except BookNotFoundError as e:
    print(f"Handled error: {e}")

try: 
    library.checkout_book(3,1)
except MemberNotFoundError as e:
    print(f"Handled error: {e}")


try:
    library.checkout_book(2,2)
except BookAlreadyCheckedOutError as e:
    print(f"Handled error: {e}")

results = library.find_book_by_title("Sapiens")
print(results)
print(type(results))

# print(results.title) # Attribute error

# results = library.find_book_by_title("Nonexistent Book")
# print(results)          # should show []
# print(results[0])       # should raise IndexError

#if results: works because an empty list is falsy in Python, and a non-empty list is truthy — so this single check protects you from both the empty-list
results = library.find_book_by_title("I am an Athiest")
if results:
    print(results[0].title)
else:
    print("No book found with that title")



# try:
#     library.return_book(2,2)
# except BookNotCheckedOutError as e:
#     print(f"Handled error: {e}")

# try:
#     library.return_book(2,2)
# except BookNotCheckedOutError as e:
#     print(f"Handled error: {e}")

# try:
#     library.checkout_book(43, 43)
# except LibraryError as e:
#     print(f"Handled error: {type(e).__name__} - {e}")

# try:
#     library.checkout_book(43, 43)
# except LibraryError as e:
#     print(f"Edge Case")



