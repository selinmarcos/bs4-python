#CODIGO SCRAPY UTILIZANDO BeautifulSoup

from numpy import histogram2d
import re
import requests
import pandas as pd
from os.path  import basename #Usamos nombre aleatorio
from googletrans import Translator
url0 = "http://www.silep.gob.bo/norma/2/ley_actualizada"
page = requests.get(url0)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

cuerpo = soup.find("div", {"class":"documento-ley"})
# print(cuerpo)


# encontrando elemento padre
h0 = soup.find("b",string="Titulo : ").parent
#ocultando elementos innecesarios
h1 = h0.text.replace('Titulo : ', '')
print(h1)
#encontramos el div que no queremos incluir
cuerpoD = cuerpo.find("div",{"class":"encabezado-descripcion col-md-12"})
#lo reemplazamo por un espacio vacio
cuerpoE = str(cuerpo).replace(str(cuerpoD),'')
#reemplazamos esta otra etiqueta que no queremos por un espacio vacio
cuerpoF = cuerpoE.replace('<br/><html><head><title>Leyes de Bolivia</title></head><body><br/>','')
# print(cuerpoF)





import json
import base64

url = 'https://leyes.abogadosbolivia.xyz/wp-json/wp/v2'
user = 'leyes'
password = '0H5h kcen XwMQ mF7C Lyj0 QX4Q'

creds = user + ':' + password
token = base64.b64encode(creds.encode())
header = {'Authorization': 'Basic ' +  token.decode('utf-8')}


#INSERTANDO EL POST
post = {
    'title' : h1,
    #ponemos str() por problemas de espacios en los parrafos para que asi se pueda copiar todo el codigo enter. ARREGLAR EN UN FUTURO !!!
    #CON IMAGEN 'content' : '<!-- wp:paragraph -->' + cuerpo.text + '<!-- /wp:paragraph --><!-- wp:image --><figure class="wp-block-image"><img src="'+ imageURL+'" alt="'+h1encabezado.text+'" title="'+h1encabezado.text+'"></figure><!-- /wp:image -->',
    'content' : '<!-- wp:paragraph -->' + cuerpoF + '<!-- /wp:paragraph -->',
    'status' : 'publish'

    # 'excerpt':'PRUEBITA'
    # 'meta': {'description': 'this is a test meta field'}
}
r = requests.post(url + '/posts', headers=header, json=post)
print (r)





