import time
import datetime as dt


#Trabajando en una version sin librerias externas

if __name__ == '__main__':

    hora_inicial = 0
    hora_final = 5
    nombre_proceso = "steam.exe"

    while 1:

        time.sleep(180)#wait 3 minutes
        hora = dt.datetime.now().hour

        if hora_inicial < hora < hora_final: #ejecuta entre hora_inicial y hora_final
            pass


