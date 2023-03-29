import threading
from sensor import Sensor

x = threading.Thread(target=Sensor, args=(1, 2)) #criando thread para o sensor 1
y = threading.Thread(target=Sensor, args=(2, 2)) #criando thread para o sensor 2
z = threading.Thread(target=Sensor, args=(3, 2)) #criando thread para o sensor 3

x.start() #iniciando thread sensor 1
y.start() #iniciando thread sensor 2
z.start() #iniciando thread sensor 3