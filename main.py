#! /usr/bin/env python3
# CPSC-440 Project
# Brendan Wang and Katelyn Choi

import adafruit_dht
import time
import board
from espeakng import ESpeakNG

dhtSensor = adafruit_dht.DHT22(board.D4, False)
esng = ESpeakNG()
esng.voice = 'gmw/en-us'

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
    except RuntimeError:
        continue

    print("The temperature is currently ", end="")
    print(temp_c, end="")
    print(" degrees Celcius.")
    print("Humidity: ", end="")
    print(humidity)
    print("==============================")
    converted_num = str(temp_c)
    converted_hum = str(humidity)
    esng.say(converted_num)
    time.sleep(2)
    esng.say('degrees celsius')
    time.sleep(2)
    esng.say('Humidity is')
    time.sleep(1)
    esng.say(converted_hum)
    time.sleep(10)