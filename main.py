import numpy as np
from read_data import Library
import functools

def run(filename):

    n_books_total, n_libraries, D, books_scores, libraries = Library.read_csv(filename)

    ordered_b_scores = np.sort(np.array([books_scores], [list(range(len(books_scores)))], axis = 1))

    d = 0

    d_slack = [D - library.n_books / library.ship - library.signup_process for library in libraries] 

    submission=[]

    scanned_books = set()

    while d < D:

        to_scans, library_scores = wrapScore(libraries, d_slack, scanned_books, books_scores)

        chosen_library = np.arg_max(library_scores)[0] # max index over library score array array 

        libraries[chosen_library].n_books = set()

        to_scan = to_scans[chosen_library]

        scanned_books.add(to_scan) # check!

        submission.append((chosen_library,to_scan))

        d = d + chosen_library.signup_process

        d_slack = d_slack-chosen_library.signup_process


def wrapScore(library, d_slack, scanned_books, books_scores):

    for d_sl in d_slack:

        if d_sl < 0:

            return adj_score
        else:
            
            return functools.reduce(lambda x, y: books_scores[x] + books_scores[y]  ,library.books - scanned_books) / library.signup_process










def adj_score(library):
    to_check = library.books-scanned_books
    to_scan = top_scoring(to_check, library.ship*(D-d-library.signup_process))
    score = functools.reduce(lambda x, y: books_scores[x] + books_scores[y]  ,to_scan) / library.signup_process
    return to_scan, score

def    


if __name__ == "__main__":

    run('filename')
