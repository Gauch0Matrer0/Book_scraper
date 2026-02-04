from get_pages import get_pages
import sys
import prod_info
 
def count_o(argvs):
    count = 0
    for arg in argvs:
        if "-o" in arg:
            count += 1
    return count
def check_args(argvs):
    if(len(argvs) > 1):
        return "-L" in argvs or "-M" in argvs or (count_o(argvs) > 0)
    else:
        return True
def get_multiple_books():
    title = ''
    auth = ''
    book_list = []
    while True: 
        title = input("insert books title: ")
        if title == 'exit':
            return book_list
        auth = input("insert author: ")
        if auth == 'exit':
            return book_list
        book = auth, title
        book_list.append(book)


try:
    assert "-L" not in sys.argv or "-M" not in sys.argv

    assert count_o(sys.argv) <= 1

    assert check_args(sys.argv) 
except AssertionError as err:
    print("error!")

if "-L" in sys.argv:
    title = input("insert books title: ")
    auth = input("insert author: ")
    book = auth, title
    get_pages(book)
elif "-M" in sys.argv:
    book_list = get_multiple_books()
    for book in book_list:
        get_pages(book)




