my_list_original = [20,31,12,11,6,65,55,102]
'''
Genera una lista ya que está dentro de los corchetes.
En esa lista hemos realizado un bucle.
En ese bucle recoge cada dato de la variable my_list_original.
'''
my_list = [i for i in my_list_original]
print(my_list)
'''
Ha creado una lista realizando un bucle con 8 datos enumerados.
'''
my_list2 = [i for i in range(8)]
print(my_list2)
'''
Ha creado una lista en el que por cada iteración 
se multiplica el valor por dos.
'''
my_list3 = [i*2 for i in range(8)]
print(my_list3)

'''
Creamos una función que devuelva el nª pi
multiplicado por el parámetro que se le asigne.
Creamos una lista en el que por cada iteración
llegará como parámetro a la función, multiplicando
el numero pi por i.
'''
import math

def numero_pi(iteracion):
    return math.pi*iteracion

my_list4 = [numero_pi(i)for i in range(3)]
print(my_list4)
