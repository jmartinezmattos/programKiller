import time
import psutil

#Este programa sirve para que no se pueda usar steam entre la 1 am y las 5 am

if __name__ == '__main__':

    nombre_proceso = "notepad.exe"

    while 1:

        time.sleep(5)#wait 5 sec

        for process in psutil.process_iter():
             #print(process.name())
            if process.name() == nombre_proceso: #cierra el proceso con el nombre de nombre_proceso
                process.kill()
