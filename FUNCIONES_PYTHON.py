# #EXTRAE CARACTERES SEGUN SU POSICION
# url0 = "http://www.silep.gob.bo/norma/12908/ley_actualizada"
# print(url0[30:35])#resultado 12908

# #ENCUENTRA la posicion de UN CARACTER ESPECIFICO
# print(url0.rfind('tt'))# resultado 2

cantidadIteraciones = 3
reemplazar = []
i = 0
while i <= cantidadIteraciones:
    r = '.replace(r['+str(i)+'],R[{'+str(i)+'}])'
    reemplazar.append(r)
    i = i+1    # update counter 



str1 = ''.join(reemplazar)
print(str1)
cuerpoDios = cuerpoF+str1