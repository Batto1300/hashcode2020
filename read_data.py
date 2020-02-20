import csv
import numpy as np


class Library:
    def __init__(self,n_books_library, signup_process_len, ship_capacity,books):
        self.n_books = n_books_library
        self.signup_process = signup_process_len
        self.ship = ship_capacity
        self.books = books

def read_csv(file_name = "a_example.txt"):
    reader = csv.reader(open(file_name), delimiter=' ')
    n_books_total, n_libraries, days_for_scanning = _read_header(reader)
    books_scores = _read_books_scores(reader)
    i = 0
    libraries = np.empty(n_libraries,dtype=Library)
    while(i < n_libraries):
        n_books_library, signup_process_len, ship_capacity = _read_library(reader)
        books = _read_books_in_library(reader)
        libraries[i] = Library(n_books_library, signup_process_len, ship_capacity, books)
        i += 1
    return n_books_total, n_libraries, days_for_scanning, books_scores, libraries

def _read_header(reader):
    n_books_total, n_libraries, days_for_scanning = next(reader)
    return int(n_books_total), int(n_libraries), int(days_for_scanning)

def _read_books_scores(reader):
    return np.array(list(map(int,next(reader))), dtype=int)

def _read_library(reader):
    n_books_library, signup_process_len, ship_capacity = next(reader)
    return int(n_books_library), int(signup_process_len), int(ship_capacity)

def _read_books_in_library(reader):
    return set(map(int,next(reader)))


def save_csv(list_, file_name='result.txt'):
    writer = csv.writer(open(file_name,'w'),delimiter=' ')
    n_libs = len(list_)
    writer.writerow(str(n_libs))
    for index_, order in list_:
        writer.writerow([index_, len(order)])
        writer.writerow(order)

if __name__ == "__main__":
    #res = read_csv("/Users/tommaso/hashcode2020/f_libraries_of_the_world.txt")
    save_csv([(3,[2,3,4,5]),(3,[3,5,6])])