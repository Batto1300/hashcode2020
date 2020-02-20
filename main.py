import numpy as np
import read_data as r
import functools

def run(filename):

    n_books_total, n_libraries, D, books_scores, libraries = r.read_csv(filename)


    arr = np.array([books_scores, list(range(len(books_scores)))])
    ordered_b_scores = np.sort(arr, axis = 1)

    d = 0

    d_slack = np.array([D - library.n_books / library.ship - library.signup_process for library in libraries])

    submission=[]

    scanned_books = set()

    while d < D:

        to_scans = [None]*len(libraries)
        library_scores = np.zeros(len(libraries))
        for i, library in enumerate(libraries):
            to_scans[i], library_scores[i] = wrapScore(library, d_slack, scanned_books, books_scores, D, d, ordered_b_scores)


        chosen_library = np.argmax(library_scores) # max index over library score array array 

        libraries[chosen_library].n_books = set()

        to_scan = to_scans[chosen_library]

        scanned_books.union(to_scan) # check!

        submission.append((chosen_library,to_scan))

        chosen_lib = libraries[chosen_library]

        d = d + chosen_lib.signup_process

        d_slack = d_slack-chosen_lib.signup_process


def wrapScore(library, d_slack, scanned_books, books_scores, D, d, ordered_b_scores):

    for d_sl in d_slack:

        if d_sl < 0:

            return adj_score(library, d_slack, scanned_books, books_scores, D, d, ordered_b_scores)
        else:
            to_scan = library.books - scanned_books
            print(books_scores)
            print(list(to_scan))
            sum_ = sum([books_scores[i] for i in list(to_scan)])
            print(sum_)
            print()
            return to_scan, sum_ / library.signup_process




def top_scoring(books, ordered_b_scores, n):

    top_books = -np.ones(n)

    count = 0
    
    for i in range(len(ordered_b_scores)):

        while count < n:

            if ordered_b_scores[i,1] in books:

                top_books[count] = ordered_b_scores[i,1]

                count += 1






def adj_score(library, d_slack, scanned_books, books_scores, D, d, ordered_b_scores):
    to_check = library.books-scanned_books
    to_scan = top_scoring(to_check, ordered_b_scores, library.ship*(D-d-library.signup_process))
    score = functools.reduce(lambda x, y: books_scores[x] + books_scores[y]  ,to_scan) / library.signup_process
    return to_scan, score
   


if __name__ == "__main__":

    run("a_example.txt")
