import utime
import urequests

def bytesTimeAndTicketMS():
    totalTime = int(str(utime.time()) + str(utime.ticks_ms()))
    totalTimeEncode = totalTime.to_bytes( 10, 'big' )

    return totalTimeEncode

#Contador del bucle
iteration = 0

#Bucle infinito
while True:
    iteration = iteration + 1
    print("Enviando dato", iteration)
    #Envío del dato (Tiempo actual en milisegundos de la respuesta de la llamada)  
    print("Valor del dato aproximado: ", int(str(utime.time()) + str(utime.ticks_ms())))
    s.send(int(str(utime.time()) + str(utime.ticks_ms())).to_bytes( 8, 'big' ))
    print("Dato enviado :D Num: ", iteration)
    