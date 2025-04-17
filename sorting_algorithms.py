import pandas as pd

# Bubble Sort Algorithm
def bubble_sort(books_df, key):
    for i in range(len(books_df) - 1):
        for j in range(len(books_df) - 1 - i):
            if books_df.iloc[j][key] > books_df.iloc[j + 1][key]:
                books_df.iloc[j], books_df.iloc[j + 1] = books_df.iloc[j + 1], books_df.iloc[j]
    return books_df

# Selection Sort Algorithm
def selection_sort(books_df, key):
    for i in range(len(books_df)):
        min_index = i
        for j in range(i + 1, len(books_df)):
            if books_df.iloc[j][key] < books_df.iloc[min_index][key]:
                min_index = j
        books_df.iloc[i], books_df.iloc[min_index] = books_df.iloc[min_index], books_df.iloc[i]
    return books_df

# Merge Sort Algorithm
def merge(left, right, key):
    merged = []
    # Ensure the DataFrames are not empty
    while not left.empty and not right.empty:
        # Compare the first element from both DataFrames based on the sorting key
        if left.iloc[0][key] < right.iloc[0][key]:
            merged.append(left.iloc[0].to_dict())  # Convert row to dictionary
            left = left.iloc[1:]
        else:
            merged.append(right.iloc[0].to_dict())  # Convert row to dictionary
            right = right.iloc[1:]
    
    # If there are any remaining rows in left or right, add them to merged
    merged += left.to_dict(orient="records")  # Convert remaining rows of 'left' to list of dicts
    merged += right.to_dict(orient="records")  # Convert remaining rows of 'right' to list of dicts
    
    # Return as DataFrame
    return pd.DataFrame(merged)

def merge_sort(books_df, key):
    if len(books_df) > 1:
        mid = len(books_df) // 2
        left_half = books_df[:mid]
        right_half = books_df[mid:]
        
        # Recursively divide the data
        left_half = merge_sort(left_half, key)
        right_half = merge_sort(right_half, key)

        return merge(left_half, right_half, key)
    else:
        return books_df

# Quick Sort Algorithm
def quick_sort(books_df, key):
    if len(books_df) <= 1:
        return books_df
    pivot = books_df.iloc[0][key]
    less_than_pivot = books_df[books_df[key] < pivot]
    greater_than_pivot = books_df[books_df[key] > pivot]
    return pd.concat([quick_sort(less_than_pivot, key), books_df[books_df[key] == pivot], quick_sort(greater_than_pivot, key)])
