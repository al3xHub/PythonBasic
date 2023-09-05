'''
Un set NO es ORDENADA, guarda elementos DESORDENADOS
No admite valores/datos repetidos.
Es modificable.
'''
mi_set = set()
print(type(mi_set))
mi_otro_set = {}#Inicialmente es un diccionario sin datos.
'''
Aquí es un set por que no hemos asignado una keyword
para cada dato como ocurre con un diccionario.
'''
mi_otro_set = {"Alejandro", "Bueno", 31}
print(type(mi_otro_set))

mi_otro_set.add("al3xHub")
print(mi_otro_set)
mi_otro_set.add("al3xHub")
print(mi_otro_set)

#Sentencia para saber si un dato está en nuestro set, devuelve un boolean.
print("Alejandro" in mi_otro_set)#Distingue mayusculas
print("Alejand" in mi_otro_set)

mi_otro_set.clear()#Borra todos los elementos.
print(len(mi_otro_set))
del mi_otro_set#Borra la variable.

mi_set = {"Alejandro", "Bueno", 31}
mi_list = list(mi_set)#Hemos convertido nuestro set en lista.

set1 = {"Rojo", "Rosa", "Azul", "Verde"}
my_new_set =  mi_set.union(set1)#unimos dos sets(No se duplica mismos datos)
print(my_new_set)

print(my_new_set.difference(set1))#Resta set1 de my new set.

