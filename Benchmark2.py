import utime
import urequests

def zfill(s, width):
    if len(s) < width:
        return ("0" * (width - len(s))) + s
    else:
        return s

# Configuración del socket bidireccional (downlinkmode) 
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

#Modo de bloqueo del Socket
s.setblocking(True)

#Contador del bucle
iteration = 0

#Bucle infinito
while True:
    iteration = iteration + 1
    print("Enviando dato", iteration)
    if iteration == 1:
        dateInicio = bytes(str(utime.time()), 'utf8')
        ticksMsInicio =  bytes(zfill(str(utime.ticks_ms()),10), 'utf8')
        print("Enviando fecha inicial... ")
        s.send(dateInicio)
        print("Fecha inicial enviada:",dateInicio)
        print("Enviado ticksMs inicial...")
        s.send(ticksMsInicio)
        print("ticksMs inicial enviado:",ticksMsInicio)
    else:
        #Envío del dato (ticks ms actual =  Milisegundos desde el inicio del dispositivo)  
        s.send(bytes(zfill(str(utime.ticks_ms()),10), 'utf8'))
        print("Dato enviado :D Num: ", iteration)

