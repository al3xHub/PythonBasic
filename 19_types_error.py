#Syntax error
#print "me llamo Python" Error
print("me llamo Python")

#NameError
#print(name) ERROR
name = "me llamo Luis"
print(name)

#IndexError
my_list=["Java", "SQL", "Python", "Javascript", "Shell"]
#print(my_list[32]) ERROR
print(my_list[2])

#ModuleNotFoundError
#import maths ERROR
import math

#AttributeError
#print(math.PI) ERROR
print(math.pi)

#KeyError
my_dict={"nombre":"Alejandro","apellidos":"Bueno Viñan",
         "edad":31, "alias":"(sin alias)"}
#print(my_dict["nacionalidad"]) ERROR
print(my_dict["alias"])

#TypeError
#print(my_list["Java"]) ERROR
print(my_list[0])

#ImportError
#from math import PI ERROR
from math import pi

#ValueError
#my_int = int("10 años") ERROR
my_int = int("10")
print(my_int)

#ZeroDivisionError
print(4/2)
#print(4/0) ERROR