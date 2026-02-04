import urllib.request
import urllib.error
import sys
import re 
from pathlib import Path
import os

def get_pages(libro):
    opener = urllib.request.build_opener()
    opener.addheaders = [('user-agent', 'myapp/1.0')]
    urllib.request.install_opener(opener)

    auth = libro[0]
    title = libro[1]

    temp = " ".join(libro)
    temp = temp.split()
    libro = "-".join(temp)
    url_base = "https://listado.mercadolibre.com.ar/"

    count = 0
    cwd = Path.cwd()
    
    while True:
        try:
            url_end = f"_Desde_{(count*48)+1}_NoIndex_True"
            url = url_base + libro + url_end    
            page = urllib.request.urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")

            start_pattern = re.compile(r"\"application/ld\+json\"")
            start_match = start_pattern.search(html)
            start = start_match.group()
            start_index = html.find(start)
            started_text = html[start_index:]

            end_index = started_text.find("</script>")
            text = started_text[:end_index - 1]
            
            
            file = str(cwd) + "/pages/" + "_meli_" + libro + str(count+1)
            print(f"writing html of {url} to {file}")
            with open(file,"w") as f:
                f.write(f"title: {title};\tauthor: {auth};\n")
                f.write(text)

            count += 1

        except urllib.error.HTTPError as err:
            return "end of pages reached"

