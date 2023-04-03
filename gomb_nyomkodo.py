import machine
import time
led = machine.Pin(2, machine.Pin.OUT)
gomb_megnyom = machine.Pin(0, machine.Pin.IN)

while True:
    if gomb_megnyom.value() == 0:
        led.on()
        print("LED is ON...\t",gomb_megnyom.value())
        time.sleep(1)
    elif gomb_megnyom.value() == 1:
        led.off()
        print("LED is OFF...\t",gomb_megnyom.value())
        time.sleep(1)
