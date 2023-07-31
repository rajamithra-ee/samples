def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")

    book = {
        "Title": title,
        "Author": author,
        "Genre": genre
    }

    library[title] = book
    print(f"Book '{title}' has been added to the library.")

def list_books(library):
    print("\n--- List of Books ---")
    if not library:
        print("The library is empty.")
    else:
        for book_title, book_info in library.items():
            print(f"Title: {book_info['Title']}")
            print(f"Author: {book_info['Author']}")
            print(f"Genre: {book_info['Genre']}")
            print("---------------------")

def search_book(library):
    title = input("Enter the title of the book you want to search: ")
    if title in library:
        book_info = library[title]
        print("\n--- Book Found ---")
        print(f"Title: {book_info['Title']}")
        print(f"Author: {book_info['Author']}")
        print(f"Genre: {book_info['Genre']}")
        print("---------------------")
    else:
        print("Book not found in the library.")

def main():
    library = {}  # The library will be stored in a dictionary.

    while True:
        print("\n--- Mini Library Menu ---")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Book by Title")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            list_books(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            print("Exiting the library. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
