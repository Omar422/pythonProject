# Week seven challenge - QUESTION NO.1.2
"""
Create a class (Library) has two attributes (shelf,book)
    book: number of books in the Library
    shelf: number of bookshelves in the Library

Create a class (section_science) which is a chlid class from the Library:
    it has one attribute (name = Physics books)

Change the book value to 20 and the shelf value to 4 in the chlid class
"""
print("Week 7 Challenge ")

class Library:

    def __init__(self,book,shelf):
        self.mybooks = book
        self.myshelves = shelf

class section_science(Library):

    def __init__(self,book,shelf,name):
        super().__init__(book, shelf)
        self.myname = name

    def printInfo(self):
        print("the number of books in the Library:",self.mybooks)
        print("the number of bookshelves in the Library:",self.myshelves)
        print(self.myname)

l1 = section_science(300, 45, "Physics books")
l1.mybooks = 20
l1.myshelves = 4
l1.printInfo()
