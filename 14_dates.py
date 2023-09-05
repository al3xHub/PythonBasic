from datetime import datetime

now = datetime.now()

print(now.minute)
print(now.second)
print(now.day)
print(now.month)
print(now.year)

timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023,1,1)

def print_date(date):
    print(now.minute)
    print(now.second)
    print(now.day)
    print(now.month)
    print(now.year)

print_date(now)

from datetime import time
current_time = time()

diff = year_2023-now
print(diff)

#Sirve para operar y trabajar distintas fechas.
from datetime import timedelta
'''
Puedes asignar directamente con ej: weeks.
o si sigues el patrón el primer parámetro será dias,
el segundo segundos etc...
'''
time_delta = timedelta(200,100,100, weeks=10)
time_delta1 = timedelta(300,50,120, weeks=9)
print(time_delta-time_delta1)



