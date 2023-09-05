'''
Con una lista podemos hacer distintas operaciones,
con distintos datos, añadiendo, eliminando etc...
Mientras que un array tiene una forma más inamovible
o sólida.
'''
mi_lista = [34, 21, 30, 31, 16, 19]
my_list = list()

print(mi_lista)
print(len(mi_lista))

my_list = [31, 1.65, "Alejandro", "Bueno"]
print(my_list)
print(type(mi_lista))
print(type(my_list))
print(my_list[2])
print(my_list[-1])
print(mi_lista.count(30))#Cuántas veces aparece ese dato

#asigna cada variable a una posicion de la lista
edad, altura, nombre, primer_apellido = my_list 
print(altura) 
print(my_list + mi_lista)

#Añade otro dato a la lista
my_list.append("Viñan")
my_list.insert(0,"Rojo")
print(my_list)
my_list.remove("Rojo")
print(my_list) 

lista_numeros = [30,30,21,31,28,19]
lista_numeros.remove(30)#Ha eliminado un valor 30 de los 2 que hay.
print(lista_numeros)
lista_numeros.pop()#Elimina el último elemneto
lista_numeros.pop(3)#Elimina el número de la posición
'''
La diferencia entre pop y del es que con pop podemos imprimir
la linea de código utilizada para que nos muestre
cuál es el dato que hemos eliminado en el último caso el nº 21

También podemos decir que con remove eliminamos indicando
el dato que conocemos. Mientras que con del indicamos su posición.
'''
del lista_numeros[0]#Elimina el elemento de esa posición
print(lista_numeros)

mi_otra_lista = my_list.copy()
print(mi_otra_lista)
mi_otra_lista.reverse()
print(mi_otra_lista)
mi_otra_lista.sort() #Ordena pero no soporta números con cadenas.
print(mi_otra_lista)


#Puedo cambiar el tipo de dato de la lista a otro. !Cuidado con este uso!
my_list = "hola Python"
print(my_list)
print(type(my_list))
