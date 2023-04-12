import network
import machine
import socket
import urandom

# WirFi személyes adatai
SSID = "wifi"
WIFI_PASSWORD = "Ervin"


# WirFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    pass

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# HTML NEM egy programozási nyelv!
html = """
<!DOCTYPE html>
<html>
    <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <title>ESP32 vezérlés</title>
           <meta
    </head>
    <body> <h1 style="color: black;">GPIO vezérlés</h1>
           <p><a href="/?pin=on"><button>BEKAPCSOL</button></a></p>
           <p><a href="/?pin=off"><button>KIKAPCSOL</button></a></p>
           <p><a href="/?stop"><button>STOP</button></a></p>
           <p><a href="/?color"><button>color</button></a></p>
    </body>
</html>
"""

# Random színek
color = "black"
colors = ["red", "green", "blue", "purple", "orange", "black"]

print(wifi.ifconfig()[0])

# Ez a megoldás akkor jó csak, ha a vezérlő kifejezetten webserver, mást nem csinál.
while True:
    conn, addr = s.accept()
    print('Kapcsolódás:', addr)
    request = conn.recv(1024)
    request = str(request)
    print('Kérés:', request)
    pin_on = request.find('/?pin=on')
    pin_off = request.find('/?pin=off')
    if request.find("/?color") == 6:
        old_color = color
        color = urandom.choice(colors)
        print(color)
        html = html.replace('<h1 style="color: ' + old_color + ';">GPIO vezérlés</h1>', '<h1 style="color: ' + color + ';">GPIO vezérlés</h1>')
    if pin_on == 6:
        print('GPIO2 BEKAPCSOLVA')
        machine.Pin(2, machine.Pin.OUT).on()
    if pin_off == 6:
        print('GPIO2 KIKAPCSOLVA')
        machine.Pin(2, machine.Pin.OUT).off()
    if request.find('/?stop') == 6:
        break
    response = html
    conn.send(response)
    conn.close()
