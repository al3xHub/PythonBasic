#Conjunto de valores constantes, inmutable.
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (35, 1.65, "Alejandro", "Bueno", "Bueno")
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Bueno"))
print(my_tuple.index("Alejandro"))#Nos dice en que posición del indice está.
mi_tupla = (2, 4, 15, 25)
print(mi_tupla + my_tuple)#Si se podrá sumar.
del my_other_tuple
print(my_other_tuple)#Error por que se eliminó la variable.