# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"{item} was not found"



book1 = Book("The hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the philosopher's stone", "J.K. Rowling", 223)
book3 = Book("The lion, the Witch and The wardrobe", "C.S. lewis", 172)

print(book2["b"])
