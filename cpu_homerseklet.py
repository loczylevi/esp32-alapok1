import esp32

homerseklet = esp32.raw_temperature()

atvaltas = (homerseklet - 32) / 1.8

