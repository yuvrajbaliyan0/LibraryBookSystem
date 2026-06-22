#Main class where all Feature are added of LibraryBookSystem
class Library:
    #constructor
    def __init__(self):
        self.books = []

    #Add Function for book in self.books....................
    def add_book(self,Book):
        self.books.append(Book)

    #Delete Function for book from self.books................
    def remove_book(self,Book):
        self.books.remove(Book)

    #Count function for Number Of books in self.books....................
    def total_book(self):
       return len(self.books)
    
    #Categorize function of book by genre.................................
    def filter_by_genre(self,genre):
        filteredlist = []
        for book in self.books:
            if book.genre == genre:
                filteredlist.append(f"{book.name} by {book.author}")
        return filteredlist

#class of book basic information....................
class Book:
    #Constructor
    def __init__(self,name,author,genre):
        self.name = name
        self.author = author
        self.genre = genre

    #convert or display list in text
    def __str__(self):
        return f"{self.name}, {self.author}, {self.genre}"



#Manager of book
stack = Library()

#ADD Book in Self.books-------------------------------------------------------------------------------------------------------------------------

#Book1
book1 = Book("48 Law Of Power","Robert Greene","Self Help")
stack.add_book(book1)

#Book2
book2 = Book("Haunting Adeline","H.D. Carlton","Dark Romance")
stack.add_book(book2)

#Book3
book3 = Book("The Predator","RuNyx","Dark Romance")
stack.add_book(book3)

#Book4
book4 = Book("Atomic Habits","James Clear","Self Help")
stack.add_book(book4)

#Book5
book5 = Book("To Kill a Mockingbird","Harper Lee", "Fiction")
stack.add_book(book5)

#Book6
book6 = Book("Pride and Prejudice","Jane Austen","Fiction")
stack.add_book(book6)

#REMOVE BOOK FROM self.books..............................................................................................................................
stack.remove_book(book3)


#Display or print all Book in self.books//////////////////////////
for book in stack.books:
    print(book)
        
#COUNT NUMBER OF BOOK IN self.books........................................................................................................................
Count = stack.total_book()
print(Count)

#Filter or Categorize Books by genre........................................................................................................................
for book in stack.filter_by_genre("Self Help"):
    print(book)


