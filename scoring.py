
def top_scoring(books, books_scores, n):

    top_books = set()

    count = 0
    
    for i in range(len(books_scores)):

        while count < n:

            if books_scores[i,1] in books:

                top_books.add(books_scores[i,1])

                count += 1