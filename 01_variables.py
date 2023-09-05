'''
Es siempre en minúsculas

Ejemplos:

firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
'''
my_int = 5
print(type(my_int)) #type nos dice el tipo de dato (int,string,boolean...)
print(my_int)
my_string = "Lobitos tiene la loba"
print(my_string)
my_bool = True
print(my_bool)

#Concatenar variables.
print(my_bool,my_int,my_string)
print("5 Lobitos tiene la loba??", my_bool)
print(f"{my_int} lobitos tiene la loba?? {my_bool}")

'''
Cambio de tipo int a string
con el "str" delante podemos cambiar el tipo de dato.
En este caso de entero a cadena.
'''
int_to_string = str(my_int)
print(type(int_to_string))
print(int_to_string)

#Función len, nos cuenta números de caracteres
print(len(my_string))# "Lobitos tiene la loba" tiene 21.

#Variables en una sola línea
name, surname, alias, age = "Alejandro", "Bueno Viñan", "Al3x", 31
print("Mi nombre es",name,surname,"y mi edad es de",age,"pero todos me llaman",alias)

#Insertar datos por teclado
primer_apellido = input("Cuál es tu primer apellido?: ")
edad = input("¿Y tu edad?: ")
print(primer_apellido)
print(edad)


