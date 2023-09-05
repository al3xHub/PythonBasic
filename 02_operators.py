print(3+5)
print(3-5)
print(3*5)
print(3/5)
print(10%2)#Operador de módulo, obtiene el resto de una división
print(5//3)#El resultado nos da el número entero más proximo
print(3**3)#Exponente

print("hola"+"python")#Se puede concatenar strings con sumar
print("Python "*3)
print("Python "*(2**4))
'''
Para sumar string con enteros debes hacer esto ya que convierte int por 
string. No se puede hacer sin hacer esto.
'''
print("hola"+str(5))

#Operaciones de comparación
print(3<4)
print(3>4)
print(3<=4)
print(3>=4)
print(3==4)
print(3!=4)

#Está comparando cada caracter.
print("Comparacion entre cadenas")
print("Hola"<"Python")
print("hola">"python")
print("hola"<="bola")#Comparó alfabeticamente ASCII
print(len("hola") <= len("bola"))#Comparó por números de carácteres con la función "len".
print("hola">="python")
print("hola"=="Hola")#Distinguió entre mayúsculas y minúsculas. ASCII
print("hola"!="python")

'''
Operadores lógicos
and, or, not.
'''
print("Operadores lógicos")
print(3>4 and "hola">"python")
print(3<4 and "hola"<"python")
print(not(3>4))#"Lo contrario de 3 menor que 4 es verdadero(True)"