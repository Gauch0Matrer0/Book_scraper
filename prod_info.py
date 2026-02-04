import re
import os
from pathlib import Path
#go into scraper.py and add get_info after everything

def score(prod_name, title, author):
    prod_name = prod_name.lower()

    score = 1
    title.split()
    count = 0
    for word in title:
        if word.lower() in prod_name:
            count +=1
    if count == len(title):
        score += 1

    author.split()
    count = 0
    for word in author:
        if word.lower() in prod_name:
            count += 1
    if count == len(author):
        score += 1  
    
    return score

def get_info():
    print("getting info")
    path_to_pages = str(Path.cwd()) + "/pages/"
    pages = os.listdir(path_to_pages) 
    open(path_to_pages + "products", "w")

    i = 0
    final_list = []
    for item in pages:

        
        page = path_to_pages + item
        with open(page,"r") as file:
            text = file.read()

        title_pattern = re.compile(r"title:([^;]*);")
        title_match = title_pattern.search(text)
        title = title_match.group(1)
        auth_pattern = re.compile(r"author:([^;]*);")
        auth_match = auth_pattern.search(text)
        author = auth_match.group(1)

        storage = text.split("\"@type\":\"Product\"")
        del storage[0]

        name_pattern = re.compile(r"\"name\":\"([^\"]*)\"")
        price_pattern = re.compile(r"\"price\":(\d*)")
        for product in storage:
            i += 1
            price_match = price_pattern.search(product)
            price = price_match.group(1)
            name_match = name_pattern.search(product)
            prod_name = name_match.group(1)
            buffer = prod_name, int(price), score(prod_name, title, author)
            final_list.append(buffer)

        print(title,"\n",author)
    return final_list
