def my_function():
    print("Esto es una función")
my_function()

def sumar(primero,segundo):
    print(primero+segundo)

sumar(5,4)

def sumar_return(primero,segundo):
    return(primero+segundo)

'''
En este ejemplo el resultado que es 7 simplemente se retorna
'''
sumar_return(5,2)
'''
Aquí estamos sacando en pantalla el retorno del método
que es 5.
'''
print(sumar_return(2,3))
'''
También podemos guardar el retorno en una variable para 
hacer lo que queramos, por ejemplo sacarlo con un print.
En este caso saldra el resultado 15.
'''
my_return = sumar_return(5,10)
print(my_return)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Bueno", name="Alejandro")

'''
En esta función podemos asignar un parámetro
predeterminado, en este caso en el parámetro alias.
Si no escribimos nada al llamar a la función, saldrá
el valor predeterminado.
'''
def print_name2(name,surname,alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name2("Alejandro","Bueno")

'''
De esta forma con un solo parámetro podremos añadir más
de un dato a esta función. Imprimirá todas las cadenas
de texto.
'''
def print_texto(*texto):
    print(texto)

print_texto("hola", "que tal?")



