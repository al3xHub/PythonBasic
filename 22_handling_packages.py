#pip
import numpy #pip install numpy
print(numpy.version.version)
num_array=numpy.array([22,31,13,65,126,785])
print(type(num_array))

import pandas #pip install pandas

#pip list (lista de los paquetes)
#pip uninstall pandas
#pip show numpy (mostrar info sobre numpy u otros paquetes)
#pip install request

import requests
#response=requests.get("")
#print(response)
#print(response.status_code)

#Nuestro paquete creado.
from mypackage import arithmetics
print(arithmetics.sum_values(8,8))
