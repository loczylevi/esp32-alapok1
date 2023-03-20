import esp32
def get_celz():
    homerseklet = esp32.raw_temperature()
    return (homerseklet - 32) / 1.8

lista = []
for i in range(500):
    print(i**4)
    print(get_celz())
    lista.append(get_celz())
tarolo = []  
for szam in lista:
    if szam > 42.77778:
        tarolo.append(szam)
        
