def print_book_description(title, author, publisher, year, version, num_pages):
    print('The book has the title', title)
    print('The book has the author', author)
    print('The book has the publisher', publisher)
    print('The book has the year', year)
    print('The book has the version', version)
    print('The book has the num_pages', num_pages)


# print_book_description('The Lord of The Rings', 'J. R. R Tolkien', 'George Allen & Uwin',
#                        1954, 1.0, 456)

# This below function call can give incorrect output because we forgot the order
# of the arguments

# print_book_description('J. R. R Tolkien', 'The Lord of The Rings', 'George Allen & Uwin',
#                        1954, 1.0, 456)


# keyword argument

print_book_description(author='J. R. R Tolkien', title='The Lord of The Rings', publisher='George Allen & Uwin',
                       year=1954, version=1.0, num_pages=456)

















