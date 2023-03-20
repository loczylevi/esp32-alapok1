import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
tarolo = {}
index = 1
for scans in wlan.scan():
    tarolo.update({index: scans[0:2]})
    index = index + 1
    

for x, y in tarolo.items():
  print(x, "ESSID:", y[0].decode(),"\tMAC cim",y[1])
