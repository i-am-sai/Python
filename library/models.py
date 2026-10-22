class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author   # Instance Variable: lives as long as the object does
        self.is_checked_out = False # Local Variable: dies when __init__ returns

# Explanatin for constructor and self keyword: 
# self is just a regular variable that refers to the specific instance being created or acted upon.
# So when constructor Book is called to create a object book1 and when during that call 3 above arguments will be passed inside constructor.
# self uses the keywords given as arguments and store in the same for that particular object (Ex: b1 = Book(11, "A", "B")) -> b1.book = A and if second object b2.book = "B".
# So it just attaches the attributes for that particular object and stores that in memory.
# only book_id = local var inside this constructor without self that value vanishes after init finishes running

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}', checked_out={self.is_checked_out})"

    def to_dict(self):
        return{
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author
        }

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    
    def __repr__(self):
        return f"Member(id={self.member_id}, name='{self.name}', borrowed_books={self.borrowed_books})"

# __repr__() provides a clear, unambiguous representation of an object, mainly for developers and debugging.
# print(book) → __str__() if available, otherwise __repr__()
# __repr__() is an inherited built-in method defined by Python's base object class. When you define your own __repr__() in your class, you are overriding the default implementation.


