import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

lista = []
for szam in range(0,100):
    lista.append(szam)


for szam in lista:
    if szam % 2 == 0:
        led.on()
        time.sleep(2)
        print("blinking is PROGRESS: DOWN please WAIT...")
    elif szam % 2 != 0:
        led.off()
        time.sleep(2)
        print("blinking is PROGRESS: UP please WAIT...")
    
print("Blinking is DONE...")
