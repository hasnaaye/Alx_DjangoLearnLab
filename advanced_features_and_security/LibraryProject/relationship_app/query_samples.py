from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Explicit query
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

# 2. List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToMany access
        print(f"\nBooks in {library.name} Library:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

# 3. Retrieve the librarian for a library (explicit query)
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # ✅ Explicit query
        print(f"\nLibrarian of {library.name} Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'")

# --------- Run Sample Queries ---------
if __name__ == "__main__":
    get_books_by_author("George Orwell")
    get_books_in_library("Central Library")
    get_librarian_of_library("Central Library")
