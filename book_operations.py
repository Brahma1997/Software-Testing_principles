import pandas as pd

# Function to add a book to the collection

def add_book(df_books, title, author, genre, year):
    new_book = pd.DataFrame({"title": [title], "author": [author], "genre": [genre], "year": [year]})
    df_books = pd.concat([df_books, new_book], ignore_index=True)
    return df_books


# Function to remove a book from the collection
def remove_book(df_books, title):
    df_books = df_books[df_books["title"] != title]
    return df_books
