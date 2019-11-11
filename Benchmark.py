import time
import urequests

# Configuración del socket bidireccional (downlinkmode) 
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

#Modo de bloqueo del Socket
s.setblocking(True)

#URL del la API que devuelve un JSON {time: Date.now()} en milisegundos
urlAPITime = "http://elrefugiodelaesquina.es:3000/api/timemilis"
#Variable para restar un byte el tiempo en milisegundos, pues son 13 cifras (bytes) y si no no entra
restaSizeTime = 1000000000000
#Contador del bucle
iteration = 0

#Bucle infinito
while True:
    iteration = iteration + 1
    print("Enviando dato", iteration)
    #Envío del dato (Tiempo actual en milisegundos de la respuesta de la llamada)  
    s.send(str(urequests.get(urlAPITime).json()['time'] - restaSizeTime).encode())
    print("Dato enviado :D Num: ", iteration)