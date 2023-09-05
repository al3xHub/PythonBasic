try:    
    print(1+"5")
except:
    print("se ha producido un error")

try:
    #Empieza a ejecutarse aquí    
    print(1+5)
except:
    #Se ejecuta si hay un error
    print("se ha producido un error")
else:
    #Se ejecuta si no hay ningun error
    print("El código se ejecuta correctamente")
finally:
    #Se ejecuta siempre
    print("La ejecución del programa continúa")

#Tipos de errores
try:
    #Empieza a ejecutarse aquí    
    print(1+"2")
except TypeError as e: 
    #Imprime a parte de la cadena con la variable e tenemos la descripción del tipo de error
    print("se ha producido un error TypeError",e)



