class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        print(f"Book '{self.title}' is being deleted.")

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# Example usage
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)
    print(book)
    print(repr(book))