class LibraryError(Exception):
    pass # Base class for all library related exception
# Inherits from pythons built in Exception feature

class BookNotFoundError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BookAlreadyCheckedOutError(LibraryError):
    pass

class BookNotCheckedOutError(LibraryError):
    pass

class OptionNotFoundError(LibraryError):
    pass

# Exception = a ready-made error template.
# LibraryError = your library's generic error.
# MemberNotFoundError = a more specific library error.
# pass = "I don't need to add anything new; just use the inherited behavior."
# Python class or funciton expects something inside it if nothing yet just write pass





