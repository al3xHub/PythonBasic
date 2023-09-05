'''
Def init es lo mismo que el constructor en Java.
En clase Persona tendremos dos parámetros que se estableceran
cuando en una variable instanciamos el objeto Persona con 
los valores que queramos atribuirle.
'''
class Persona:
    def __init__(self,name,surname):
        self.nombre = name
        self.apellidos = surname

my_person = Persona("Alejandro","Bueno")
print(my_person.nombre)

'''
En clase Persona2 añadimos dos propiedades que iran ya definidos
cuando llamemos a la propiedad de esa clase.
'''
class Persona2:
    def __init__(self):
        self.nombre = "Pepe"
        self.apellidos = "Fernandez"
    def walk(self):
        print(f"{self.nombre} esta caminando")
        
my_person = Persona2()
print(f"{my_person.nombre}")
