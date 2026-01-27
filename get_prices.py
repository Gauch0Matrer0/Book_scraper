import re
from os import listdir


path_to_pages = "/home/void/Escritorio/Python/scraper/pages/"
pages = listdir(path_to_pages)

i = 0
for item in pages:
    
    page = path_to_pages + item
    with open(page,"r") as file:
        text = file.read()

    storage = text.split("\"@type\":\"Product\"")
    del storage[0]

    name_pattern = re.compile(r"\"name\":\"([^\"]*)\"")
    price_pattern = re.compile(r"\"price\":(\d*)")

    for product in storage:
        i += 1
        price_match = price_pattern.search(product)
        price = price_match.group()
        name_match = name_pattern.search(product)
        name = name_match.group()
        with open(path_to_pages + "products", "a") as products_file:
            products_file.write(f"{i}. {name}\t{price}\n")
