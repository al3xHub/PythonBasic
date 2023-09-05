print("Hola PYTHON!!")
# esto es un comentario
'''
aqui tambien puedo poner un comentario entre estas tres comitas
de esta forma
puedo escribir
en
varias
lineas :)
'''
my_string = "Esto es una variable"
my_string = "ahora cambio mi variable"

#Define el tipo de variable que es
print(type(my_string))
print(my_string)

#Es de tipado dinámico
my_string = 18
print(type(my_string))
print(my_string)

my_string = "Alejandro"
my_int = 24
my_booleano = True

#Concatenar frases con las variables
print(f"Mi nombre es {my_string} y tengo {my_int} años. Y el booleano es {my_booleano}")

#Arrays
my_list = [my_booleano,my_int,my_string]
print(type(my_list))
print(my_list)
print(my_list[2])

#Los diccionarios asignan una cable a cierto dato, variable etc...
my_diccionario = {"boleano": my_booleano,"int":my_int,"cadenita": my_string, "yatusabe": "Ouhyeahhh"}
print(type(my_diccionario))
print(my_diccionario["cadenita"])
print(my_diccionario["yatusabe"])

'''Los sets es un array que impide meter valores ya repetidos
va en llaves en vez de corchetes
he escrito la variable my_string varias veces pero al salir en la consola
solamente aparece el valor (Alejandro) una vez.
Es una estructura DESORDENADA igual que los diccionarios
'''
my_set = {my_booleano,my_int,my_string,my_string,my_string,my_string,my_string,my_string,my_string}
print(type(my_set))
print(my_set)

'''
En las tuplas si podemos poner valores repetidos y son ORDENADOS como en las listas.
La diferencia entre la tupla y la lista es que en la lista podemos añadir mas valores una vez creada la lista
con la tupla no ocurre eso.
'''
my_tupla = (my_booleano,my_int,my_string,my_string,my_string,my_string,my_string,my_string,my_string)
print(type(my_tupla))
print(my_tupla)

#Condicionales
#and , or , not
if my_int == 23 and my_booleano == True:
 print("El valor si es 23 y el boleano es verdadero")
elif my_int == 24 or my_booleano == False:
 print("No es 23 pero si el boleano es falso")
else:
 print("El valor es incorrecto")

for i in my_list:
  print(i)

for i in range(10):
  print(i)

#Funciones
def my_funcion():
 print("Esto es una función cabesa")

my_funcion()

for i in range(11):
 my_funcion()


'''
En esta función hemos añadido un parametro.
Retorna 1 más el parametro que le pongamos.
Hemos instanciado una variable con valor de la función creada.
Asi podemos imprimir en consola el valor del retorno.
'''
def funcion_con_retorno(param):
 return 1 + param

variable_retorno = funcion_con_retorno(30)
print(variable_retorno)

#Clases
class MyClase:
 my_name = ""

 def __init__(self, my_name):
  self.my_name = my_name
 def print_name(self):
  print(self.my_name)



my_class = MyClase("Pepe")
my_class.print_name()
my_class.my_name = "Pepito"
print(type(my_class))
print(my_class.my_name)




