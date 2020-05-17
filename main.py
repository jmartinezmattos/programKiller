import time
import datetime as dt
import psutil

if __name__ == '__main__':

    hora_inicial = 0
    hora_final = 0
    nombre_proceso = "steam.exe"

    while 1:
        ##os.system("TASKKILL /F /IM notepad.exe")
        time.sleep(10)#wait 3 minutes
        hora = dt.datetime.now().hour
        #print(hora)

        if hora_inicial < hora < hora_final: #ejecuta entre hora_inicial y hora_final
            for process in psutil.process_iter():
                #print(process.name())
                if process.name() == nombre_proceso: #cierra el proceso con el nombre de nombre_proceso
                    process.kill()
