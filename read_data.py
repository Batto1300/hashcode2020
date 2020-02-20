import csv
import numpy as np


class Library:
    def __init__(self,n_books_library, signup_process_len, ship_capacity,books):
        self.n_books_library = n_books_library
        self.signup_process_len = signup_process_len
        self.ship_capacity = ship_capacity
        self.books = books

def read_csv(file_name = "a_example.txt"):
    reader = csv.reader(open(csv_file), delimiter=' ')
    n_books_total, n_libraries, days_for_scanning = _read_header(reader)
    books_scores = _read_books_scores(reader)
    i = 0
    libraries = []
    while(i < n_libraries):
        i += 1
        n_books_library, signup_process_len, ship_capacity = _read_library(reader)
        books = _read_books_in_library(reader)
        libraries.append(Library(n_books_library, signup_process_len, ship_capacity, books))
    libraries = 
    return n_books_total, n_libraries, days_for_scanning, books_scores, libraries

def _read_header(reader):
    n_books_total, n_libraries, days_for_scanning = next(reader)
    return int(n_books_total), int(n_libraries), int(days_for_scanning)

def _read_books_scores(reader):
    return np.array(next(reader), dtype=int)

def _read_library(reader):
    n_books_library, signup_process_len, ship_capacity = next(reader)
    return n_books_library, signup_process_len, ship_capacity

def _read_books_in_library(reader):
    return set(next(reader))

if __name__ == "__main__":
    read_csv()
