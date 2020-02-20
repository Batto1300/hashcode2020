import numpy as np
from read_data import Library
import functools

def run(filename):

    n_books_total, n_libraries, D, books_scores, libraries = Library.read_csv(filename)

    d = 0

    d_slack = [D - library.n_books / library.ship - library.signup_process for library in libraries] 

    submission=[]

    scanned_books = set()

    library_scores = np.zeros(n_libraries) # store score of each library

    while d < D:

        to_scans, scores = wrapScore(libraries, d_slack, scanned_books, books_scores)

        chosen_library = np.arg_max(library_scores)[0] # max index over library score array array 

        scanned_books.add(chosen_library.books) # check!

        submission.append((chosen_library,to_scans[chosen_library]))

        d = d + chosen_library.signup_process

        d_slack = d_slack-chosen_library.signup_process


def wrapScore(library, d_slack, scanned_books, books_scores):

    for d_sl in d_slack:

        if d_sl < 0:

            return adj_score
        else:
            
            return functools.reduce(lambda x, y: books_scores[x] + books_scores[y]  ,library.books - scanned_books) / library.signup_process




def top_scoring(books, books_scores, n):

    top_books = np.array(n)

    count = 0
    
    for i in range(len(books_scores)):

        while count < n:

            if books_scores[i,1] in books:

                top_books[count] = top_books[books_scores[i,1]]

                count += 1






def adj_score(library):

    pass



    


if __name__ == "__main__":

    run('filename')
