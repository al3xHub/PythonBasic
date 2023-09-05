'''
Es como una función anónima, sin nombre.
'''
sum_dos_valores = lambda primer_valor,segundo_valor: primer_valor+segundo_valor
print(sum_dos_valores(2,4))

'''
Añadimos en una función una lambda.
La funcion tiene un parámetro y la lambda 2.
Cuando llamemos a la función pondremos entre parentesis
primero el primer parámetro de la función
seguido de parenéntesis con los parámetros de la lambda.
'''
def sumar_tres_valores(value):
    return lambda primer_valor, segundo_valor: primer_valor+segundo_valor+value

print(sumar_tres_valores(5)(2,4))