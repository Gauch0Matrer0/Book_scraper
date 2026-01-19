import re

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


