# write a library with no_of books and books as two instance variable.
# write a program to create a library from this library class and show
# how you can print all books, add a book and get the number of book using
# different method.#

class library:
    def __init__(self):
        self.No_of_book = 0
        self.books = []
    
    def Add_book(self,book):
        self.books.append(book)
        self.No_of_book = len(self.books)
        
    def Show_book(self):
        print(f"The library has {self.No_of_book} books.\nThe books are:\n")
        for book in self.books:
            print(book)
            
#num = int(input("Enter the number of book:"))
lib = library()
#for book in range(0,num):
lib.Add_book("Harry potter")
lib.Add_book("Devin night")
lib.Add_book("Dark knight")
    
lib.Show_book()
        
        
    
    