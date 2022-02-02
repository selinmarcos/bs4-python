#CODIGO SCRAPY UTILIZANDO BeautifulSoup
from unidecode import unidecode
import urllib.parse
from urllib.parse import urlparse
import unicodedata
import re
from numpy import histogram2d
import re
import requests
import pandas as pd
from os.path  import basename #Usamos nombre aleatorio
from googletrans import Translator
url0 = "http://www.silep.gob.bo/norma/6/ley_actualizada"
page = requests.get(url0)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
data = {}

cuerpo = soup.find("div", {"class":"documento-ley"})

#encontramos el div que no queremos incluir
cuerpoD = cuerpo.find("div",{"class":"encabezado-descripcion col-md-12"})
#lo reemplazamo por un espacio vacio
cuerpoE = str(cuerpo).replace(str(cuerpoD),'')
#reemplazamos esta otra etiqueta que no queremos por un espacio vacio
cuerpoF = cuerpoE.replace('<br/><html><head><title>Leyes de Bolivia</title></head><body><br/>','')
# print(cuerpoF)
R=[]
r=[]
#VERIFICANDO SI HAY LINKS
if soup.find_all("a",{"style":"cursor:pointer;"}) == []:
    print('NO LINKS')
else:    
    cuerpoLink = soup.find_all("a",{"style":"cursor:pointer;"})
    for i in cuerpoLink:
        #extraemos el codigo de ley de los links
        p = str(i)
        a1 = '('
        a2 = ','
        b1= p.rfind(a1)
        b2 = p.rfind(a2)
        nEnlace = p[b1+1:b2]
        print(nEnlace)

        #EXTRAEMOS EL H1 DE nEnlace para formar la url que incrustaremos en el link

        url1 = f'http://www.silep.gob.bo/norma/{nEnlace}/ley_actualizada'
        print(url1)
        pageLink = requests.get(url1)    
        soupLink = BeautifulSoup(pageLink.content, 'html.parser')

        # encontrando elemento padre
        e0 = soupLink.find("b",string="Titulo : ").parent
        #ocultando elementos innecesarios
        e1 = e0.text.replace('Titulo : ', '')+'-bolivia'
        print(e1)

        my_str = e1[1:].lower().replace(' ','-')
       


        urlaInsertar = f'http://leyes.abogadosbolivia.xyz/{my_str}'
        print(urlaInsertar)

        #reemplazamo el valor de onclick
        
        c1 = 'on'
        c2 = ')'
        d1= p.rfind(c1)
        d2 = p.rfind(c2)
        nOnclick = p[d1:d2+2]
        print(nOnclick)
        resultadoR = p.replace(nOnclick,f'href="{urlaInsertar}"')

        # cuerpoDios = cuerpoF.replace(p,resultadoR)
        R.append(resultadoR)
    print(R)

    for j in cuerpoLink:
        r.append(str(j))
    print(r)

    print(len(r))



    if len(r) == 1:
        cuerpoDios=cuerpoF.replace(r[0],R[0])
    elif len(r) == 2:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1])
    elif len(r) == 3:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2])
    elif len(r) == 4:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3])
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]).replace(r[5],R[5])
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4]) 
    elif len(r) == 5:
        cuerpoDios=cuerpoF.replace(r[0],R[0]).replace(r[1],R[1]).replace(r[2],R[2]).replace(r[3],R[3]).replace(r[4],R[4])      
        
    else:
        print('error')

        


# encontrando elemento padre
h0 = soup.find("b",string="Titulo : ").parent
#ocultando elementos innecesarios
h1 = h0.text.replace('Titulo : ', '')+' Bolivia'
# print(h1)


#AUN PROCEDE ????????????????????????????????????????????????????? AL PARECER NO!
# # CONVIRTIENDO A URL VALIDA 
# my_str = 'http://leyes.abogadosbolivia.xyz/'+h1[1:].lower().replace(' ','-')
# # my_str = quote(my_str, safe="%/:=&?~#+!$,;'@()*[]")

# #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA    
# urlH1 = my_str

# #Armando el Dictionary key value 
# c1 = 'a/'
# c2 = '/l'
# p1= url0.rfind(c1)
# p2 = url0.rfind(c2)
# codigoLey = url0[p1+2:p2]
# data[codigoLey] = urlH1

# # print(data)




try: 
    cuerpoFinal = cuerpoDios
except: 
    cuerpoFinal = cuerpoF




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
    'content' : '<!-- wp:paragraph -->' + cuerpoFinal + '<!-- /wp:paragraph -->',
    'status' : 'publish'

    # 'excerpt':'PRUEBITA'
    # 'meta': {'description': 'this is a test meta field'}
}
r = requests.post(url + '/posts', headers=header, json=post)
print (r)





