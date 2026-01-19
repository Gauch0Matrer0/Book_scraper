import re

state = 0
char_count = 0
word_count = 0
buffer = []
storage = []


with open("pages/3","r") as f:
    html = f.read()

start_pattern = re.compile(r"<script type=\"application/ld\+json\" nonce=\".*?\"")
start_match = start_pattern.search(html)
start = start_match.group()
start_index = html.find(start)
started_text = html[start_index + len(start) + 2 :]

end_index = started_text.find("</script>")
text = started_text[:end_index - 1]

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

for product in buffer:
    print(product)
    price_pattern = re.compile(r"\"price\":(\d*)")
    price_match = price_pattern.search(product)
    price = price_match.group()
    
    name_pattern = re.compile(r"\"name\":\"([^\"]*)\"")
    name_match = name_pattern.search(product)
    name = name_match.group

   # print(f"{buffer.index(product)}. {name} - {price}")


