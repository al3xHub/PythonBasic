'''
Inspecciona si una cadena de texto tiene elementos.
'''

#match

import re
my_string = "Esta es una cadena de texto con mayúsculas y minúsculas, con 9 palabras."
my_other_string = "Esta es otra cadena de texto, con esta cadena podemos trabajar con ella."
#Encuentra un patrón
'''
Busca desde el principio del string
nos dice que entre el carácter 0 y 18 encuentra el patrón.
'''
print(re.match("Esta es una cadena",my_string))
print(re.match("Esta es una cadena",my_other_string))
'''
Podemos ver muchos métodos con re, en este por ejemplo
ignora mayúsculas y minúsculas.
'''
match=print(re.match("Esta es una cadena",my_string, re.I))
if not match==None:
    print(match)
    start, end = match.span()#span devuelve el comienzo y final de una tupla
    print(my_string[start:end])
    

#search
'''
encuentra la cadena que esta en cualquier parte del texto,
NO desde el principio como con match.
'''
search=re.search("texto", my_string,re.I)
print(search)

#findall(listado con las veces que lo ha encontrado)
findall = re.findall("con", my_string,re.I)
print(findall)

#split
'''
Divide la cadena de texto en otro index empezando por
los carácteres encontrados "es".

En cada "es" se dividirá por otro index.
'''
split=re.split("es", my_string)
print(split)

#sub(substituye como su nombre indica)
print(re.sub("cadena", "CADENA", my_other_string))
print(re.sub("cadena", "CADENA", my_other_string))

#patrones
print(re.sub("[e|E]sta", "ESTA", my_string))
'''
con "r" por delante indicamos que es un patrón/expresión regular.
'''
pattern=r"[e|E]sta"
print(re.findall(pattern, my_other_string))
pattern=r"[e|E]sta|cadena"
print(re.findall(pattern, my_other_string))
pattern=r"[0-9]"
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))
pattern=r"\d"
print(re.findall(pattern, my_string))

#email validation
email="alejandro2023@msn.com"
fake_email="alejandro.com.es"
pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.match(pattern, fake_email))
