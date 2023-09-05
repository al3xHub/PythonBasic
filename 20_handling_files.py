#.txt file
import os
'''
"r" permite leer el fichero 
(Puedes bucar "python file modes)
"r+" Se puede leer y escribir.
'''
#txt_file = open("PythonBasico/my_file.txt","r+")
#print(txt_file.read())
#print(txt_file.read(10)) #Lee primeros 10 char.
#print(txt_file.readline()) #Lee primera linea
#print(txt_file.readline()) #Lee segunda linea
#print(txt_file.readlines())# Mete cada linea en un array
#for i in txt_file.readlines():
#    print(i)
'''
escribe sobre la línea que nos hemos quedado en el código
si no hubiese hecho el bucle for y leido todas las lineas
no hubiera escrito en la última línea, si no al principio.
OJO!
'''
#txt_file.write("\nAunque también me gusta Java")

txt_file = open("PythonBasico/my_file.txt","w+")
txt_file.write("Mi nombre es Alejandro\nY mi apellido es Bueno\nTengo 31 años\nMi lenguaje de programación favorito es Python\n")
for i in txt_file.readlines():
    print(i)
txt_file.write("Aunque también mola Javascript")
txt_file.close()

'''
Para eliminar el fichero
os.remove("PythonBasico/my_file.txt")
'''

#.json file
import json
file_json = open("PythonBasico/my_json.json","w+")
json_text={"tipo": "camiseta", "marca":["Nike","Nike Air","Nike Air Jordan"],
           "precio":32.99, "temporada": "2023-2024"}
#Así se crea el fichero JSON
#indent se utiliza para darle espacios y saltos de linea.
json.dump(json_text,file_json, indent=2)
file_json.close()

with open("PythonBasico/my_json.json") as my_other_file:
    for i in my_other_file.readlines():
        print(i)

#Pasamos el json a un diccionario
json_dict = json.load(open("PythonBasico/my_json.json"))
print(json_dict)
print(type(json_dict))

#.csv file
import csv
csv_text = {"name":"Lola", "surname":"Aguilar Morilla",
            "age":31, "nacionality":"Spanish"}
csv_file = open("PythonBasico/my_csv.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","nacionality"])
csv_writer.writerow(["Lola","Aguilar Morilla","31","Spanish"])
csv_file.close()
'''
Habíamos creado el fichero, ahora vamos a leerlo.
'''
with open("PythonBasico/my_csv.csv") as my_other_csv:
    for i in my_other_csv.readlines():
        print(i)
#.xlsx file
#Se necesita modulo externo al core de python
#.xml file
import xml