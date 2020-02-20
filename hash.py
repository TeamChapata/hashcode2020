import numpy as np
import math
import sys


def read_file(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        n_books, n_libraries, n_days = [int(n) for n in line.split()]

        line = f.readline()
        books_score = [int(n) for n in line.split()]

        data_libraries = np.zeros([n_libraries, 3])
        libraries_books = np.zeros([n_libraries], dtype=object)
        for library in range(n_libraries):
            line = f.readline()
            data_libraries[library, :] = [int(n) for n in line.split()]
            line = f.readline()
            libraries_books[library] = [int(n) for n in line.split()]
        return n_books, n_libraries, n_days, data_libraries, libraries_books, books_score


""""
IN:
    - id_book: Id of last choosen book
    - books_score: Array to save the score of each book
    - used_books: Array to save if a book is already used or not
    - actual_score: Actual score of the solution
RETURN:
    Updated actual_score
"""
def update_score(id_book, books_score, used_books, actual_score):
    if not used_books[id_book]:
        return actual_score + books_score[id_book]


def main():
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    print('Running on file %s' % sys.argv[1])

    n_books, n_libraries, n_days, data_libraries, libraries_books, books_score = read_file(sys.argv[1])


if __name__ == '__main__':
    main()
