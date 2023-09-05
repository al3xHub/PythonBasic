#While
contador  = 0
while contador <10:
    print(contador)
    contador +=1
else:
    print("mi condición es igual o mayor que 10")

contador1 = 0
while contador1 <10:
    print(contador1)
    contador1 +=1
    if contador1 ==6:
        print("Se detiene en 6")
        break

#For
my_list = [1,14,53,44,32,78]

for i in my_list:
    print(i)
else:
    print("Ya se imprimió todo")

for i in my_list:
    print(i)
    if i == 14:
        break

for i in my_list:
    print(i)
    if i == 14:
        print("Hola")
        continue
else:
    print("El bucle ha finalizado")

