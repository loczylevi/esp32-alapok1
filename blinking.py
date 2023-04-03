import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

szamlalo = 0
while szamlalo < 10:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    szamlalo = szamlalo + 1
    print("blinking is PROGRESS: ",szamlalo, "sec please WAIT...")
    
print("Blinking is DONE...")
