'''
Escribe un programa que muestre por consola los números
de 1 a 100, sustituyendo los siguientes:
 -Multiplos de 3 por la palabra "fizzz"
 -Multiplos de 5 "buzz"
 -Multiplos de 3 y 5 "fizzbuzzz"
'''
for i in range(1,101):
    if i %3 ==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz") 
    else:
        print(i)

'''
Escribe una función que reciba dos palabras y
retorne verdadero o falso segun sea o no anagramas.
    Un anagrama trata de formar una palabra re-
    ordenando TODAS las letras de otra palabra inicial
'''

def es_anagrama(palabra1,palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    elif sorted(palabra1.lower())==sorted(palabra2.lower()) :
        return True

print(es_anagrama("Amor","Roma"))

'''
Escribe un programa que imprima los 50 primeros numeros
de la sucesion de fibonnaci
 - Los numeros son la suma del anterior:
    0,1,1,2,3,5,8,13...
'''
def fibo():
    prev = 0
    next = 1
    for i in range(50):
        print(prev)
        fib = prev+next
        prev=next
        next=fib
fibo()
print("Fibonacci 2")
def fibo2():
    a, b = 0, 1
    for i in range(50):
        print(a)
        a, b = b, a+b

fibo2()
'''
0
0+1=1
1=1
1=1

1
1+1=2
1=1
1=2

1
1+2=3
1=2
2=3t

2
2+3=5
2=3
3=5

3
'''

'''
Escribe un programa que se encargue de comprobar si es 
un numero primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''
def primo():
    for number in range(1,101):
        if number >= 2:
            divisible = False
            for i in range(2, number):
                if number % i == 0:
                    divisible = True
                    break
            if not divisible:
                print(number)

primo()
'''
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje q lo haga automático
si pasamos "hola mundo" nos retornaría "odnum aloh"
'''
def reverse(texto):
    texto_len = len(texto)
    reversed_texto = ""
    for i in range(0,texto_len):
        reversed_texto += texto[texto_len-i-1]
    return reversed_texto

print(reverse("hola mundo"))