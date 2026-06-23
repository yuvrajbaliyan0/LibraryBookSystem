#An Library Book System
class Library:
    def __init__(self):
        self.Books = []
    
class Book:
    def __init__(self,Name,Author,Genre):
        self.name = Name 
        self.author = Author 
        self.genre = Genre 
    def __str__(self):
        return{self.name,self.author,self.genre}

stack = Library()

#Book1
book1 = Book("It Ends With Us","Colleen Hoover","Romance")
#Book2
book2 = Book("Pride and Prejudice","Jane Austen","Romance")
#Book3
book3 = Book("Project Hail Mary","Andy Weir", "Sci-fi")
#Book4
book4 = Book("The Hunger Games","Suzanne Collins", "Sci-fi")

#Book5
book5 = Book("Atomic Habit","James Clear", "Self-Help")

#Book6
book6 = Book("The 5 AM","Robin Sharma","Self-Help")

