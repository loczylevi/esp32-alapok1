"""

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
tarolo = {}
index = 1
for scans in wlan.scan():
        tarolo.update({index: scans[0:2]})
        index = index + 1
    

for x, y in tarolo.items():
  print(x, "ESSID:", type(y[0].decode()),"\tMAC cim",y[1])
  
"""
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
lista =  ["galaxy","samsung","poco","xiaomi","honor","tek","redmi"]

for scan in wlan.scan():
    if any(sel in scan[0].decode().lower() for sel in lista):
        print("ESSID: ", scan[0].decode(), " \t|\t MAC: ", scan[1])
