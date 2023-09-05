my_string = "cadena de texto con comillas"
my_other_string = 'cadena de texto con comillas simples'

print('"yes, they said"')#Manera de imprimir las comillas en consola

print(my_string)
print(my_other_string)

#Con "len" sabemos cuántos carácteres hay
print(my_other_string,"tiene",len(my_other_string),"carácteres")

caracteres_especiales1 = "Esto es una frase\ncon salto de línea"
caracteres_especiales2 = "Esto es una frase\tcon tabulación"
print(caracteres_especiales1,caracteres_especiales2)
 
#Format
nombre, apellido, edad = "Alex", "Bueno", 31
print("Mi nombre es {} {} y mi edad es {}".format(nombre,apellido,edad))
#%s es un string y %d es un entero
print("Mi nombre es %s %s y mi edad es %d" %(nombre,apellido,edad))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

#Desempaquetado de caracteres
lenguaje = "python"
a, b, c, d, e , f = lenguaje
print(a)
print(f)

#División
lenguaje_slice = lenguaje[0:3]
print(lenguaje_slice)#Ha cogido la letra 0, 1 y 2
lenguaje_slice = lenguaje[1:]# de la 1 hasta el final
print(lenguaje_slice)
lenguaje_slice = lenguaje[-2]# Cuenta de derecha a izq
print(lenguaje_slice)

#Reverse
reverse_lenguaje = lenguaje[::-1]
print(reverse_lenguaje)

#Funciones
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))#cuantas "t" tiene
print(lenguaje.isnumeric())
# y muchas más... mirar en documentación python.org o 30 days with Python (GitHub)
