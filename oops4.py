# This is a demo for showing encapsuation and abstraction examples in python
# Here the method call is the abstraction and the logic has been encapsulated within it.

class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayBooks(self):
        print("The books available are as below:")
        for i in self.availableBooks:
            print(i)

    def lendBook(self, lentBook):
        if lentBook in self.availableBooks:
            self.availableBooks.remove(lentBook)
            print("The book is has been lent now.")
        else:
            print("The book is not available in the library.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("Thank you the book - {} has been returned to the library.".format(returnedBook))


class Customer:

    def requestBook(self):
        print("Enter the name of the book to be borrowed : ", end="")
        self.option = input()
        return self.option

    def returnBook(self):
        print("Enter the name of the book to be returned : ", end="")
        self.book = input()
        return self.book

#This is only for testing the functionality
lib1 = Library(["Hello World","Jobs - Steven Paul Jobs","The monk who sold his Ferarri"])
cust1 = Customer()
lib1.displayBooks()
req = cust1.requestBook()
lib1.lendBook(req)
print("")
lib1.displayBooks()
print("")
lib1.addBook(req)
print("")
lib1.displayBooks()

#Originally what you can do is provide options for the user.
