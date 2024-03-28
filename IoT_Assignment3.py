import paho.mqtt.publish as publish
import time
import random
import datetime

channelID = "2488618"
apiKey = "8RF8FHFCKD6J1VWH"
clientID = "AyUlIBgPFA4ICxoFBCQVIgI"
clientUSERNAME  = "AyUlIBgPFA4ICxoFBCQVIgI"
clientPASSWORD  = "gwmuw5L5MW3DHhhMOheheQJL"
host = "mqtt3.thingspeak.com"
TRANSPORT = "websockets"
port = 80
topic = "channels/" + channelID + "/publish"

while True:
    temperature = random.uniform(-50, 50)
    humidity = random.uniform(0, 100)
    co2 = random.uniform(300, 2000)

    payload = "field1={:.2f}&field2={:.2f}&field3={:.2f}".format(temperature, humidity, co2)
    print("___________________________READINGS___________________________")
    print("")
    print("Temperature:",temperature)
    print("Humidity:",humidity)
    print("Pressure:",co2)
    print("")

    print("Data Published to ThingSpeak successfully! ")
    print("")

    publish.single(topic, payload, hostname=host, transport=TRANSPORT, port=port, client_id=clientID, auth={'username':clientUSERNAME,'password':clientPASSWORD})
    
    time.sleep(5)  #Publish data every 5 seconds
