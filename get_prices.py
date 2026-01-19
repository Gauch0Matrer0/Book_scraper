import re
from os import listdir

pages = listdir("/home/void/Escritorio/Python/scraper/pages")
for item in pages:
    
    page = "/home/void/Escritorio/Python/scraper/pages/" + item
    with open(page,"r") as file:
        text = file.read()

    state = 0
    buffer = []
    storage = []

    for c in text:
        if (c == '{'):
            state = 1
        elif(c != '{' and c != '}' and state == 1):
            buffer.append(c)
        elif(c == '}'):
            state = 0
            buffer = "".join(buffer)
            storage.append(buffer)
            buffer = []


    with open("/home/void/Escritorio/Python/scraper/pages/all_products.txt","a") as final_file:
        for product in storage:
            final_file.write(product + '\n')

        #conseguir precios de los libros
          
        #enviarlo a un archivo con todos los libros


r"""
state = 0
buffer = []
storage = []

for c in text:
    if (c == '{'):
        buffer.append(c)
        state = 1
    elif(c != '{' and c != '}' and state == 1):
        buffer.append(c)
    elif(c == '}')
        buffer.append(c)
        state = 0
        buffer = "".join(buffer)
        storage.append(buffer)
        buffer = []

for product in buffer:
    print(product)
    price_pattern = re.compile(r"\"price\":(\d*)")
    price_match = price_pattern.search(product)
    price = price_match.group()
    
    name_pattern = re.compile(r"\"name\":\"([^\"]*)\"")
    name_match = name_pattern.search(product)
    name = name_match.group

    print(f"{buffer.index(product)}. {name} - {price}")
"""

