#CODIGO SCRAPY UTILIZANDO BeautifulSoup

from numpy import histogram2d
import re
import requests
import pandas as pd
from os.path  import basename #Usamos nombre aleatorio
from googletrans import Translator
url0 = "https://www.lostiempos.com/actualidad/mundo/20220126/presidente-peru-desata-tormenta-comentario-mar-bolivia"
urlPage="https://www.paginasiete.bo"
page = requests.get(url0)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

encabezadoH1 = soup.find("h1", {"class":"node-title"})
print(encabezadoH1.text)


table = soup.find_all(['p'])
# #eliminamos las ','
table0 = ''.join(str(table).split(','))
# #eliminamos el primer y el ultimo caracter que son '[]'
table01 = table0[1:-1]

print(table01)
# #eliminamos el parrafo de cookies
table1 = table01.replace('<p><span></span> Más en Cultura</p>', '')



# # #Buscamos la imagen y extraemos el src
# try: #img is inside div
#     imagen = soup.find_all("div", {"class": "separator"})
#     img = imagen[0].find('img').get('src')
# except: #img is inside td
#     imagen = soup.find_all("td")
#     img = imagen[0].find('img').get('src')

s = soup.find("img", {"class":"image-style-noticia-detalle"}).get('src')
print (s)
img = s[:s.rfind("?")]
# #Descargamos la imagen
# nombreImagen= imagen
with open(basename(img), "wb") as f: #Tambien podemo usar basename(img) instead of nombreImagen si queremos un nombre aleatorio.
    f.write(requests.get(img).content)
    imgName = basename(img) #guardamos el nombre de la imagen en la variable imgName






# #----------------------------------------SCRIPT PARA TRADUCIR---------------------------------------------
# trans = Translator()

# h1encabezado = trans.translate(encabezadoH1.text, src='en', dest='es')
# cuerpo= trans.translate(table1, src='en', dest='es')
# # print(h1encabezado.text)
# # print(cuerpo.text)


#------------------------SCRIPT PARA INSERTAD DATOS A WORDPRESS-----------------------------------------
import json
import base64

url = 'https://100webtools.xyz/wp-json/wp/v2'
user = '100webtools'
password = 'afpz Apv8 kazI Qeqa OUre YFRc'

creds = user + ':' + password
token = base64.b64encode(creds.encode())
header = {'Authorization': 'Basic ' +  token.decode('utf-8')}




# CODIGO PARA INSERTAR IMAGEN
media = {
    'file' : open (imgName, 'rb'), #traemos la variable imagen
}



image = requests.post(url + '/media', headers=header, files=media)
print(image)
#extrayendo postid para la featured image
postid =json.loads(image.content.decode('utf-8'))['id'] 
#realizamos doble  .post para primero poder subir la imagen y despues ponerle los atributos... 
postm={
    'title': encabezadoH1.text,
    'caption': encabezadoH1.text,
    'description': 'description',
    'alt_text': encabezadoH1.text
}
req = requests.post(url + '/media/'+str(postid), headers=header, json=postm) 




#INSERTANDO EL POST
post = {
    'title' : encabezadoH1.text,
    #ponemos str() por problemas de espacios en los parrafos para que asi se pueda copiar todo el codigo enter. ARREGLAR EN UN FUTURO !!!
    #CON IMAGEN 'content' : '<!-- wp:paragraph -->' + cuerpo.text + '<!-- /wp:paragraph --><!-- wp:image --><figure class="wp-block-image"><img src="'+ imageURL+'" alt="'+h1encabezado.text+'" title="'+h1encabezado.text+'"></figure><!-- /wp:image -->',
    'content' : '<!-- wp:paragraph -->' + table01 + '<!-- /wp:paragraph -->',
    'status' : 'publish',
    'featured_media': postid,
    
    # 'excerpt':'PRUEBITA'
    # 'meta': {'description': 'this is a test meta field'}
}
r = requests.post(url + '/posts', headers=header, json=post)
print (r)




