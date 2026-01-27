import re

with open("out.txt","r") as f:
    text = f.read()

    pattern = re.compile(r"\"application/ld\+json\"")
    match = pattern.search(text)
    print(match.group())
