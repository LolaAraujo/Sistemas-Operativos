import os
from tabulate import tabulate
import random as rd
import msvcrt as mv
import threading, time
import keyboard as kb

idProductor = 0
idConsumidor = 0
rangoBuffer=20
Buffer = ['__'] * rangoBuffer

def imprimir(productor,consumidor):
    os.system("cls")
    print("\nBuffer")
    headersB = list(range(rangoBuffer))
    proceso_bloq = [[Buffer[i] for i in headersB]]
    print(tabulate(proceso_bloq, headers=headersB, tablefmt="double_outline"))
    # print("Buffer en forma de lista",Buffer,"\n")
    print("Productor está",productor)
    print("Consumidor está",consumidor)

#exit_program = False

def verificar_esc():
    #while True:
    if kb.is_pressed('esc'):
        print("La tecla 'esc' fue presionada. Saliendo del programa.")
        os._exit(0)


def productorConsumidor():
    global Buffer
    global idProductor
    global idConsumidor

    volado =  rd.randint(1,3)
    numeros = rd.randint(4,7)

    # esc_thread = kb.start_recording()

    # sleep_thread = threading.Thread(target=verificar_esc)
    # sleep_thread.start()
    # #sleep_time = 1

    # try:
    #     time.sleep(1)
    # except KeyboardInterrupt:
    #     pass

    # sleep_thread.join()
    # kb.stop_recording(es)

    #Productor = 1
    if volado == 1:
    # print("\n\nProductor: ", numeros)
        while True:
            imprimir('intentando','durmiendo')
            for n in range(numeros):
                verificar_esc()
                elemento = Buffer[idProductor]
                if elemento != '✔':
                    Buffer[idProductor] = '✔'
                    idProductor = (idProductor+1)%len(Buffer)
                    imprimir('produciendo','durmiendo')
                    verificar_esc()
                    time.sleep(1)
                # time.sleep(1)
                else:
                    break

            break

    #Consumidor = 2
    elif volado == 2:
    # print("Consumidor: ", numeros)
        while(True):
            imprimir('durmiendo','intentando')
            for n in range(numeros):
                verificar_esc()
                elemento = Buffer[idConsumidor]
                if elemento != '__':
                    Buffer[idConsumidor] = '__'
                    idConsumidor = (idConsumidor+1)%len(Buffer)
                    imprimir('durmiendo','consumiendo')
                    verificar_esc()
                    time.sleep(1)
                else:
                    break
            break

    # Dormidos = 3
    elif volado == 3:
        verificar_esc()
        imprimir('durmiendo','durmiendo')
        time.sleep(1)


def main():
    while True:
        verificar_esc()
        productorConsumidor()


main()