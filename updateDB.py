from database import Database

db = Database(database="bancoiot", collection="sensores")

class updateDatabase:  #classe para atualizar o banco de dados
    def updateTemp(self, temp, sensor):  #função para atualizar a temperatura
       alarm = "false"   #cria uma variável para armazenar o alarme
       sens = "Temp" + str(sensor)  #cria uma variável para armazenar o nome do sensor
       filter = {"nomeSensor": sens}   #cria uma variável para armazenar o filtro
       if(temp>38): #se a temperatura for maior que 38, o alarme é ativado
         alarm = "true"
       newTemp = {"$set": {"valorSensor": temp, "sensorAlarmado": alarm}} #cria uma variável para armazenar o novo valor da temperatura e o alarme
       db.collection.update_one(filter, newTemp) #atualiza o valor da temperatura e o alarme no banco de dados