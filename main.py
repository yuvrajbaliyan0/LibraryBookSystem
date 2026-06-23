#An Library Book System
class Library:
    def __init__(self):
        self.Books = []
    
    def add_book(self,Book):
        self.Books.append(Book)
    
    def remove_book(self,Book):
        self.Books.remove(Book)
    
    def count_book(self):
        return len(self.Books)
    
    def Filter_by_genre(self,Genre):
        FilteredBook =[]
        for book in self.Books:
            if book.genre == Genre:
                FilteredBook.append(f"{book.name} by {book.author}")
        return FilteredBook

    
    
class Book:
    def __init__(self,Name,Author,Genre):
        self.name = Name 
        self.author = Author 
        self.genre = Genre 
    def __str__(self):
        return f"{self.name},{self.author},{self.genre}"

stack = Library()

#ADD................................................................................................................

#Book1
book1 = Book("It Ends With Us","Colleen Hoover","Romance")
stack.add_book(book1)
#Book2
book2 = Book("Pride and Prejudice","Jane Austen","Romance")
stack.add_book(book2)
#Book3
book3 = Book("Project Hail Mary","Andy Weir", "Sci-fi")
stack.add_book(book3)
#Book4
book4 = Book("The Hunger Games","Suzanne Collins", "Sci-fi")
stack.add_book(book4)
#Book5
book5 = Book("Atomic Habit","James Clear", "Self-Help")
stack.add_book(book5)
#Book6
book6 = Book("The 5 AM","Robin Sharma","Self-Help")
stack.add_book(book6)

#DELETE...............................................................................................................
stack.remove_book(book2)

for book in stack.Books:
    print(book)

#COUNT.....................................................................................................................
print(stack.count_book())

for book in stack.Filter_by_genre("Self-Help"):
    print(book)



