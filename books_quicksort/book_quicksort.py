class Book:
    
    def __init__(self):
        self.title = None
        self.author = []
        self.isbn = None
        self.pages = None
        
    def __str__(self):
        output = "Title: " + self.title + "\n"
        for i in self.author:
            output += "Author: " + str(i) + "\n"
        output += "ISBN: " + self.isbn + "\n"
        output += "Pages: " + str(self.pages)
        return output
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __eq__(self, other):
        return self.pages == other.pages
        
    def add_author(self, author):
        self.author.append(author)

book1 = Book()
book1.title = "No bullshit guide to linear algebra"
book1.add_author("Ivan Savov")
book1.isbn = "0992001021" 
book1.pages = 570

book2 = Book()
book2.title = "Look Who's Back"
book2.add_author("Timur Vermes")
book2.add_author("Jamie Bulloch")
book2.isbn = "9780857054135" 
book2.pages = 384

book3 = Book()
book3.title = "Rich Dad Poor Dad"
book3.add_author("Robert T. Kiyosaki")
book3.isbn = "1612680194" 
book3.pages = 240

print(book1)
print(book2)
print(book3)

from quicksort import quicksort

library = [book1, book2, book3]
library_sorted = quicksort(library)

for i in library_sorted:
    print(i)