my_dict = dict()
print(type(my_dict))
my_dict1 = {}
my_dict1 = {1:"Alejandro", 2:"Bueno",
            3:"Viñan", "Estatura":1.65,
            "lenguaje":{"Python","Java","Javascript"}}
print(my_dict1["Estatura"])
print(my_dict1[2])
print(my_dict1["lenguaje"])
print(len(my_dict1))#Cuenta las claves, no el/los datos.
my_dict1["Estatura"] = 1.66 #Modificar un dato del diccionario.
print(my_dict1["Estatura"])

my_dict1["Peso"] = 64 #Añade una nueva clave
print(my_dict1["Peso"])
del my_dict1["Peso"] #Borra una clave 
print(my_dict1)

print("Alejandro" in my_dict1)#FALSE, hay que buscar por la clave.
print(1 in my_dict1)#Manera correcta

print(my_dict1.items())#Listado de las keyword y valores
print(my_dict1.keys())
print(my_dict1.values())

'''
Se crea un nuevo diccionario sin valores pero con 
las claves que hemos indicado sacadas de 
nuestra variable my_dict1 que es 1 y "Estatura".
'''
my_dict2 = my_dict1.fromkeys((1,"Estatura"))
print(my_dict2)
'''
Un buen uso de fromkeys es crear una variable con las keywords
de otro diccionario, en este caso de my_dict2
'''
my_dict3 = dict.fromkeys(my_dict2)
print(my_dict3)