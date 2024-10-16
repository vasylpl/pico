import machine
import time

led1 = machine.Pin(1, machine.Pin.OUT)

led2 = machine.Pin(2, machine.Pin.OUT)

led3 = machine.Pin(3, machine.Pin.OUT)

led4 = machine.Pin(4, machine.Pin.OUT)

#machine.Pin(1, machine.Pin.OUT).value(1)

while True:
    time.sleep(0.02)
    led1.value(0.02)
    time.sleep(0.1)
    led1.value(0)

    time.sleep(0.02)
    led2.value(0.02)
    time.sleep(0.1)
    led2.value(0)

    time.sleep(0.02)
    led3.value(0.02)
    time.sleep(0.1)
    led3.value(0)
    
    time.sleep(0.02)
    led4.value(0.02)
    time.sleep(0.1)
    led4.value(0)

    time.sleep(0.02)
    led4.value(0.02)
    time.sleep(0.1)
    led4.value(0)

    time.sleep(0.02)
    led3.value(0.02)
    time.sleep(0.1)
    led3.value(0)

    time.sleep(0.02)
    led2.value(0.02)
    time.sleep(0.1)
    led2.value(0)

    time.sleep(0.02)
    led1.value(0.02)
    time.sleep(0.1)
    led1.value(0)
    