import streamlit as st
import pandas as pd
from book_operations import add_book, remove_book
from sorting_algorithms import bubble_sort, selection_sort, merge_sort, quick_sort

# Sample Book Data (can be modified or expanded)
books = [
    {"title": "Book 1", "author": "Author A", "genre": "Fiction", "year": 2020},
    {"title": "Book 2", "author": "Author B", "genre": "Non-Fiction", "year": 2019},
    {"title": "Book 3", "author": "Author A", "genre": "Fiction", "year": 2021},
    {"title": "Book 4", "author": "Author C", "genre": "History", "year": 2018}
]

# Convert books data to DataFrame
df_books = pd.DataFrame(books)

# Streamlit UI
st.title("Smart Bookshelf Organizer")

# Add Book Section
st.subheader("Add a Book")
title = st.text_input("Title")
author = st.text_input("Author")
genre = st.text_input("Genre")
year = st.number_input("Year", min_value=1800, max_value=2025, value=2020)

if st.button("Add Book"):
    df_books = add_book(df_books, title, author, genre, year)
    st.success(f"Book '{title}' added successfully!")

# Remove Book Section
st.subheader("Remove a Book")
book_to_remove = st.selectbox("Choose Book to Remove", df_books["title"])

if st.button("Remove Book"):
    df_books = remove_book(df_books, book_to_remove)
    st.success(f"Book '{book_to_remove}' removed successfully!")

# Sorting Section
st.subheader("Sort Books")
sort_by = st.selectbox("Sort by", ["title", "author", "genre", "year"])

# Button for each sorting algorithm
if st.button(f"Sort by {sort_by} using Bubble Sort"):
    df_books = bubble_sort(df_books, sort_by)
    st.success(f"Books sorted by {sort_by} using Bubble Sort!")
    st.write(df_books)

if st.button(f"Sort by {sort_by} using Selection Sort"):
    df_books = selection_sort(df_books, sort_by)
    st.success(f"Books sorted by {sort_by} using Selection Sort!")
    st.write(df_books)

if st.button(f"Sort by {sort_by} using Merge Sort"):
    df_books = merge_sort(df_books, sort_by)
    st.success(f"Books sorted by {sort_by} using Merge Sort!")
    st.write(df_books)

if st.button(f"Sort by {sort_by} using Quick Sort"):
    df_books = quick_sort(df_books, sort_by)
    st.success(f"Books sorted by {sort_by} using Quick Sort!")
    st.write(df_books)

# Display Books
st.subheader("Bookshelf")
st.write(df_books)

# Book Tagging (Personalization)
st.subheader("Tag a Book")
book_to_tag = st.selectbox("Select a Book to Tag", df_books["title"])
tags = st.text_input("Enter Tags (comma separated)", "favorite, to-read")

if st.button("Tag Book"):
    for book in books:
        if book["title"] == book_to_tag:
            book["tags"] = tags
    st.success(f"Book '{book_to_tag}' tagged with {tags}")

# Data Import and Export
st.subheader("Import/Export Bookshelf Data")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df_books = pd.read_csv(uploaded_file)
    st.write("Bookshelf data loaded:")
    st.write(df_books)

# Export the current bookshelf as CSV
csv = df_books.to_csv(index=False).encode()
st.download_button(
    label="Download Bookshelf Data as CSV",
    data=csv,
    file_name="bookshelf_data.csv",
    mime="text/csv"
)
