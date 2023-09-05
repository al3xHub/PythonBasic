#Funciones dentro de otras.
from functools import reduce


def sumar_uno(value):
    return value+1
def sumar_cinco(value):
    return value+5

def sum_values(primer,segun,sum):
    return sum(primer+segun)

print(sum_values(5,2,sumar_uno))
print(sum_values(5,2,sumar_cinco))

#Closures
def sum_ten():
    def add(value):
        return value +10
    return add
closure=sum_ten()
print(closure(5))

#Buil-in Higher Order Functions
numbers = [2,5,10,21]

#Map
def multiply(num):
    return num*2

print(list(map(multiply,numbers)))
print(list(map(lambda numbers: numbers*2,numbers)))

#Filter
def filter_my10(number):
    if number>10:
        return True
    return False

print(list(filter(filter_my10,numbers)))
print(list(filter(lambda number: number>10,numbers)))

#Reduce
def sum_values(primero,segundo):
    return primero+segundo
print(reduce(sum_values,numbers))
