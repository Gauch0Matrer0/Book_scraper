"""
conseguir todas las paginas de  una busqueda:
    try abrir pagina count:
        cuerpo
        count++
    except eception as err
"""
import urllib.request
import urllib.error
import sys
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
        hmtl = html_bytes.decode("utf-8")
        
        file = "pages/"+str(count+1)
        print(f"writing html of {url} to {file}")
        with open(file,"w") as f:
            f.write(hmtl)

        count += 1

    except urllib.error.HTTPError as err:
        sys.exit("end of pages")


