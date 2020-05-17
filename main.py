import time
import datetime as dt
import psutil

#Este programa sirve para que no se pueda usar steam entre la 1 am y las 5 am

if __name__ == '__main__':

    hora_inicial = 0
    hora_final = 5
    nombre_proceso = "steam.exe"

    while 1:

        time.sleep(180)#wait 3 minutes
        hora = dt.datetime.now().hour

        if hora_inicial < hora < hora_final: #ejecuta entre hora_inicial y hora_final
            for process in psutil.process_iter():
                #print(process.name())
                if process.name() == nombre_proceso: #cierra el proceso con el nombre de nombre_proceso
                    process.kill()
