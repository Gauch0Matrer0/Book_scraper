import urllib.request
import re

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
with opener.open('https://listado.mercadolibre.com.ar/mao-tse-tung-el-libro-rojo_NoIndex_True_desde_1') as f:
   print(f.read().decode('utf-8')h 
