import urllib.request
import urllib.error
import sys
import re

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

libro = input("insertar titulo del libro: ")
templibro = libro.split()
libro = "-".join(templibro)
url_base = "https://listado.mercadolibre.com.ar/"

count = 0

while True:
    try:
        url_end = f"_Desde_{(count*48)+1}_NoIndex_True"
        url = url_base + libro + url_end    
        page = urllib.request.urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        start_pattern = re.compile(r"<script type=\"application/ld\+json\" nonce=\".*?\"")
        start_match = start_pattern.search(html)
        start = start_match.group()
        start_index = html.find(start)
        started_text = html[start_index + len(start) + 2 :]

        end_index = started_text.find("</script>")
        text = started_text[:end_index - 1]
        
        file = "/home/void/Escritorio/Python/scraper/pages/"+str(count+1)
        print(f"writing html of {url} to {file}")
        with open(file,"w") as f:
            f.write(text)

        count += 1

    except urllib.error.HTTPError as err:
        sys.exit("end of pages")


