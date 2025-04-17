# Smart Bookshelf Organizer

This project is a **Smart Bookshelf Organizer** that allows users to organize, add, remove, and sort books. The application is built using **Streamlit** and supports sorting algorithms such as **Bubble Sort**, **Selection Sort**, **Merge Sort**, and **Quick Sort**. The project is structured to allow easy configuration management, branching, and version control using **Git**.

---

## Project Structure

The project is organized into the following file structure:




### Key Files:

- **main.py**: 
    - The entry point for the application. It contains the user interface (UI) built with **Streamlit**.
    - Manages the bookshelf, user inputs, sorting options, and integrates with other files for book operations and sorting.

- **book_operations.py**: 
    - Contains functions for adding and removing books from the bookshelf.
    - Handles book management, such as appending a new book or removing an existing one.

- **sorting_algorithms.py**: 
    - Contains the implementation of the sorting algorithms.
    - **Bubble Sort**, **Selection Sort**, **Merge Sort**, and **Quick Sort** algorithms are implemented here.

- **bookshelf_data.csv**: 
    - Contains sample data for the bookshelf. It is used to populate the Streamlit app for testing.
    - You can upload a similar CSV file to the app to import/export your bookshelf data.

---

## How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone 
    cd Smart-Bookshelf-Organizer
    ```

2. **Install dependencies**:
    Ensure that **Python 3.x** is installed on your machine. Install the required libraries by running the following command:
    
    ```
    If `requirements.txt` is not present, you can install **Streamlit** and **pandas** manually:
    ```bash
    pip install streamlit pandas
    ```

3. **Run the Streamlit app**:
    After installing the necessary dependencies, run the Streamlit app with the following command:
    ```bash
    streamlit run main.py
    ```

4. **Access the application**:
    Streamlit will automatically open the application in your default web browser. If it doesn’t, open `http://localhost:8501` in your browser.

---

## Branching and Version Control

This project uses **Git** for version control. The repository follows the Git flow, with different branches for each feature.

### Branches:
- **master**: Contains the stable version of the project.
- **feature/sorting**: Contains the sorting algorithm implementation.
- **feature/adding-book-functionality**: Handles the implementation of adding new books.
- **feature/remove-book-functionality**: Handles the implementation of removing books.

To work on new features:
1. Create a new branch:
   ```bash
   git checkout -b feature/new-feature-name
