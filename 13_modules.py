import module
'''
Para importar los modulos debemos de tener un encabezado
correcto. Empezando por número no funcionaría como por ejemplo
con "import 10_modulo"
'''
module.sumar(30,13)#Debemos indicar desde donde recogemos sumar con el "." y el modulo delante.

'''
Si queremos directamente llamar al método debemos de importarlo
de otra manera.

"from module import sumar, restar, operacion1"
sumar(5,3)
'''
import math
print(math.pi)
print(math.pow(2,6))

from math import pi as piiii
print(piiii)