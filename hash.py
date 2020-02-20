import numpy as np
import math
import sys
import random as rnd


def read_file(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        n_books, n_libraries, n_days = [int(n) for n in line.split()]

        line = f.readline()
        books_score = [int(n) for n in line.split()]

        data_libraries = np.zeros([n_libraries, 3], dtype=int)
        libraries_books = np.zeros([n_libraries], dtype=object)
        for library in range(n_libraries):
            line = f.readline()
            data_libraries[library, :] = [int(n) for n in line.split()]
            line = f.readline()
            libraries_books[library] = order_books([int(n) for n in line.split()], books_score)
        return n_books, n_libraries, n_days, data_libraries, libraries_books, books_score


def order_books(books, scores):
    for i in range(len(books)):
        for j in range(len(books)-i-1):
            if scores[books[j]] < scores[books[j+1]]:
                books[j+1], books[j] = books[j], books[j+1]
    return books


def write_output(n_libraries, library_ex_info, library_books, filename):
    with open(filename, 'w') as f:
        f.write('{}\n'.format(int(n_libraries)))
        for n in range(n_libraries):
            f.write(''.join(str(item) + ' ' for item in library_ex_info[n, :]) + '\n')
            f.write(''.join(str(item) + ' ' for item in library_books[n, :]) + '\n')


# def aleatorio(max_days, library_data):
#     days_spend = 0
#     current_library_data = np.copy(library_data)
#     libraries_pos = np.zeros([current_library_data.shape[0]])
#     for n in libraries_pos:
#         libraries_pos[n] = n + 1
#     rnd.shuffle (libraries_pos)
#     n = 0
#     while n < len(libraries_pos) and (days_spend <= max_days):



def main():
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    print('Running on file %s' % sys.argv[1])

    n_books, n_libraries, n_days, data_libraries, libraries_books, books_score = read_file(sys.argv[1])

    write_output(n_libraries, data_libraries, data_libraries, sys.argv[2])

    print(libraries_books)


if __name__ == '__main__':
    main()
