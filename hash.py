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


def main():
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    print('Running on file %s' % sys.argv[1])

    n_books, n_libraries, n_days, data_libraries, libraries_books, books_score = read_file(sys.argv[1])


if __name__ == '__main__':
    main()
