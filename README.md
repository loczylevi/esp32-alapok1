# esp32-alapok1

micropython az esp32 firmware

https://micropython.org/download/esp32/

https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/

https://wokwi.com/projects/305570169692881473

https://docs.micropython.org/en/latest/esp8266/tutorial/network_tcp.html


micropython nulláról otthon átnázni!!!!

https://docs.micropython.org/en/latest/library/index.html


hozzá kell adni a felhasználót a dialout csoportba!
aztán Thony --> Tools --> Options --> Interpeter --> felül micropython esp32 --> alul a portot kell kiválasztani

sudo adduser loczylevi dialout

route -n

route

ifconfig

lsusb --> ki listazza az összes usp portot ami be van dugva a számitogépbe

cat /etc/group    --> dialouge csoportba ki tartozkodik

sudo apt remove brltty    --> a vakos mod jobb ha elvan távolitva

