import random
import time
from updateDB import updateDatabase

def Sensor(sensor, interval):
    temp = int(0)  #cria uma variável para armazenar a temperatura(inteiro)
    while True:
        if temp > 38:   #se a temperatura for maior que 38, imprime a mensagem de atenção
            print("Atenção! Temperatura muito alta! Verificar sensor", sensor)
        else:  #se não, gera uma temperatura aleatória entre 30 e 40 e atualiza no banco de dados
            temp = temp = random.randrange(30, 40) #gera uma temperatura aleatória entre 30 e 40
            print("Temperatura sensor", sensor, ":", temp)  #imprime a temperatura do sensor
            updateDatabase().updateTemp(temp, sensor)   #atualiza a temperatura no banco de dados
        time.sleep(interval)  #aguarda o tempo definido no intervalo