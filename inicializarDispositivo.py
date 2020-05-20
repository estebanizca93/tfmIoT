from network import Sigfox, WLAN
import os
import machine
import socket
import utime
import binascii

uart = machine.UART(0, 115200)
os.dupterm(uart)

#JSON con las redes wifi conocidas a las que conectarse
redesConocidas = {
    'WLAN_Esteban_Invitados': {'pwd': 'daoiz22invitados'},
}

#Conexión a una red WiFi conocida
if machine.reset_cause() != machine.SOFT_RESET:
    wl = WLAN()
    wl.mode(WLAN.STA)

    print("Buscando redes WiFi conocidas...")
    redesDisponibles = wl.scan()
    redes = frozenset([e.ssid for e in redesDisponibles])

    wifiSSIDs = frozenset([key for key in redesConocidas])
    redConocida = list(redes & wifiSSIDs)
    try:
        redConocida = redConocida[0]
        propiedadesRedes = redesConocidas[redConocida]
        pwd = propiedadesRedes['pwd']
        sec = [e.sec for e in redesDisponibles if e.ssid == redConocida][0]
        if 'wlan_config' in propiedadesRedes:
            wl.ifconfig(config=propiedadesRedes['wlan_config'])
        wl.connect(redConocida, (sec, pwd), timeout=10000)
        while not wl.isconnected():
            machine.idle() # ahorro de energía mientras se espera conexión
        print("Conectado a "+redConocida+" con dirección IP:" + wl.ifconfig()[0])

    except Exception as e:
        print("No se ha podido establecer ninguna conexión WiFi")

##Establece la hora en el dispositivo mediante una petición a servidor NTP
def setRTCLocalTime():
    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org")
    utime.sleep_ms(750)
    print('\nRTC establablecido desde NTP a UTC:', rtc.now())
    utime.timezone(7200)
    print('Ajuste de zona horaria a GMT+2', utime.localtime(), '\n')

#Estabelcer hora actual al dispositivo
setRTCLocalTime()

# Inicilizar Sigfox para la región RCZ1 (Europe) 
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1) 
 
# Creación de un Socket para establecer comuncación con Sigfox 
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
 
# Configuración de tipo de conexión unidireccional (solo subida de datos) 
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False) 

# Congifuración de bloqueo de Socket 
s.setblocking(True)