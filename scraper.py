from get_pages import get_pages

book = input("insert books name: ")
auth = input("insert author: ")
print(get_pages(auth + " " + book))

