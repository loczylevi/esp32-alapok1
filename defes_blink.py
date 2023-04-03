import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

def blinking(meddig,time_on,time_off,msg):
    szamlalo = 0
    while szamlalo <= meddig:
        led.on()
        time.sleep(time_on)
        led.off()
        time.sleep(time_off)
        szamlalo = szamlalo + 1
        print(msg)
        
    print("Blinking is DONE...")

