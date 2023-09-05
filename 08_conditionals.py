my_conditional = True

if my_conditional: #Es lo mismo que if my_conditional == True:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_conditional = 5*2

if my_conditional==10:
    print("se ejecuta la condición del segundo if")
else:
    print("No se ejecutó la segunda condición")

my_conditional = 5*3

if my_conditional==10:
    print("se ejecuta la condición del segundo if")
else:
    print("No se ejecutó la segunda condición")

my_conditional = 6

if my_conditional==5:
    print("Es igual que 5")
elif(my_conditional>5):
    print("Es mayor que 5")
else:
    print("Es menor que 5")

my_conditional = 20

if my_conditional >5 or my_conditional==20:
    print("Es igual que 5 o mayor")
elif(my_conditional<5):
    print("Es menor que 5")

my_string = "Cadena de textoooO"

if not my_string == "Cadena de texto": #Si es lo contrario de igual a "cadena de texto"
    print("Es contrario a: Cadena de texto")
elif(my_string == "Cadena de textoooO"):
    print("Es igual a: ",my_string)



