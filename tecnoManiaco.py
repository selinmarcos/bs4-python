#CODIGO SCRAPY UTILIZANDO BeautifulSoup

from numpy import histogram2d
import re
import requests
import pandas as pd
from os.path  import basename #Usamos nombre aleatorio
from googletrans import Translator
url0 = "https://www.allblogthings.com/2021/02/how-to-use-amazon-alexa-to-send-and-receive-text.html"
urlPage="https://www.paginasiete.bo"
page = requests.get(url0)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

encabezadoH1 = soup.find("h1", {"class":"entry-title"})
# print(encabezadoH1.text)


table = soup.find_all(['h2', 'p', 'ol'])
#eliminamos las ','
table0 = ''.join(str(table).split(','))
#eliminamos el primer y el ultimo caracter que son '[]'
table01 = table0[1:-1]

# print(table01)
#eliminamos el parrafo de cookies
table1 = table01.replace('<p class="image-caption excerpt">With help of our readers our aspiration is to be the best information resource &amp; an online magazine for Startups Tech Savvies Small Businesses and Entrepreneurs of every industry around the globe. We are publishing content to help everyone out there start a business or spend the day well. Stay with us!</p> <p class="gnews-pro-cookie-ify-content excerpt">Our website uses <a href="https://www.blogger.com/go/blogspot-cookies">cookies</a> to improve your experience. <a href="https://www.allblogthings.com/p/privacy.html">Learn more</a></p> <p class="contact-form-error-message" id="ContactForm1_contact-form-error-message"></p> <p class="contact-form-success-message" id="ContactForm1_contact-form-success-message"></p>', '')


# print(table1)
# table1= ", ".join( repr(e) for e in table0) 



# print(str(table))


# table = soup.find_all("div", {"id":"post-body"})
# singleP = []
# for p in table:
#     parrafo = p.find_all("p")
#     for sp in parrafo:
#         singleP.append(sp.get_text())



# #Buscamos la imagen y extraemos el src
try: #img is inside div
    imagen = soup.find_all("div", {"class": "separator"})
    img = imagen[0].find('img').get('src')
except: #img is inside td
    imagen = soup.find_all("td")
    img = imagen[0].find('img').get('src')




# #Descargamos la imagen
# nombreImagen= imagen
with open(basename(img), "wb") as f: #Tambien podemo usar basename(img) instead of nombreImagen si queremos un nombre aleatorio.
    f.write(requests.get(img).content)
    imgName = basename(img) #guardamos el nombre de la imagen en la variable imgName


#------------------------------SCRIPT TO EXPORT IN EXCEL USING PANDAS-------------------------------------------


# import numpy as np
# #import pandas as pd

# df = pd.DataFrame({
#     'Col A': [encabezado.text],
#     'Col B': [subencabezado.text],
#     'Col C': [cuerpoNota.text],
# })

# df.to_excel('df.xlsx', index=False) # para que no aparezca el index




#----------------------------------------SCRIPT PARA TRADUCIR---------------------------------------------
trans = Translator()

h1encabezado = trans.translate(encabezadoH1.text, src='en', dest='es')
cuerpo= trans.translate(table1, src='en', dest='es')
# print(h1encabezado.text)
# print(cuerpo.text)


#------------------------SCRIPT PARA INSERTAD DATOS A WORDPRESS-----------------------------------------
import json
import base64

url = 'https://tecnomaniaco.xyz/wp-json/wp/v2'
user = 'tecnomaniaco'
password = 'xI7k AOde uFm9 jIDe ZB1u eklQ'

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
    'title': h1encabezado.text,
    'caption': h1encabezado.text,
    'description': 'description',
    'alt_text': h1encabezado.text
}
req = requests.post(url + '/media/'+str(postid), headers=header, json=postm) 




#INSERTANDO EL POST
post = {
    'title' : h1encabezado.text,
    #ponemos str() por problemas de espacios en los parrafos para que asi se pueda copiar todo el codigo enter. ARREGLAR EN UN FUTURO !!!
    #CON IMAGEN 'content' : '<!-- wp:paragraph -->' + cuerpo.text + '<!-- /wp:paragraph --><!-- wp:image --><figure class="wp-block-image"><img src="'+ imageURL+'" alt="'+h1encabezado.text+'" title="'+h1encabezado.text+'"></figure><!-- /wp:image -->',
    'content' : '<!-- wp:paragraph -->' + cuerpo.text + '<!-- /wp:paragraph -->',
    'status' : 'publish',
    'featured_media': postid,
    
    # 'excerpt':'PRUEBITA'
    # 'meta': {'description': 'this is a test meta field'}
}
r = requests.post(url + '/posts', headers=header, json=post)
print (r)




