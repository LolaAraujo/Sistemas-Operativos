"""
CreatMed on Wed Aug 30 21:05:52 2023

@author: Lola&Aldo
"""
import os
from tabulate import tabulate
import random as rd
import time as t
import msvcrt as mv

IDs = []
id = 0

def cantidad_procesos():
    global numProcess
    while True:
        try:
            numProcess = int(input("\nDame un número de procesos: "))
            if 0 < numProcess <= 500:
                break
            else:
                print("\nEl número de procesos debe ser menor de 500.\n")
        except ValueError:
            print("\nNúmero Inválido.\n")

def ID():
    global id
    while True:
        id += 1
        if not id in IDs: #Comprobación de ID
            IDs.append(id)
            break

def isOperador():
    global resultado
    global operaciones

    #Recursivo y excepciones
    while True:
        num1 = rd.randint(0,100)
        num2 = rd.randint(0,100)

        opc = rd.randint(1,6)

        if opc == 1:
            operador = '+'
            resultado = num1+num2
            break

        elif opc == 2:
            operador = '-'
            resultado = num1-num2
            break

        elif opc == 3:
            operador = '*'
            resultado = num1*num2
            break

        elif opc == 4:
            if num1 > 0 and num2 > 0:
                operador = '/'
                resultado = num1/num2
                resultado = "{:.2f}".format(resultado)
                break

        elif opc == 5:
            if num1 > 0 and num2 > 0:
                operador = '%'
                resultado = num1%num2
                break

        elif opc == 6:
            if num1 > 0:
                operador = '**'
                resultado = num1**num2
                resultado = "{:.2e}".format(resultado)
                break


    operaciones = f"{num1}{operador}{num2}"


def tiempo_estimado():
    global TME
    TME = rd.randint(6,18)

def lotes_de_procesos():
    global info
    global procesos_pendientes
    global totalProces
    global contTiempo
    global Tr
    contTiempo = 0
    Tr = 0
    info = []
    procesos_pendientes=[]

    proceso = 1
    os.system("cls")
    cantidad_procesos()
    totalProces = numProcess

    while totalProces != 0:
        os.system("cls")
        ID()
        isOperador()
        tiempo_estimado()
        info = [id,operaciones,resultado,TME, contTiempo, Tr]
        procesos_pendientes.append(info)
        os.system("cls")
        totalProces -= 1
        proceso += 1    

def intoTecla():
    global tecla
    tecla='q'
    if mv.kbhit():
        tecla = mv.getch().decode('utf-8')            
        if tecla == 'p':
            os.system('cls')
            imprimir()
            print("Este programa se encuentra pausado...")
            while tecla != 'c':
                try:
                    tecla = mv.getch().decode('utf-8')
                    if tecla == 'c':
                        print("Reanudando Programa...")
                        t.sleep(1)
                        os.system('cls')
                except UnicodeDecodeError:
                    pass

def imprimir():
    global tiempo_restante
    # -------------------------- Lotes Actuales
    print("\nNo. Lotes Pendientes: ", contPendiente)
    print("\nLote Actual: ", contLote, "\t\tProceso en Ejecución \t\tProcesos Terminados")

    headersA = ["ID", "TME", "TT"]
    lote_actual_tabla = [[lista[0], lista[3], lista[4]] for lista in lote_actual]
    tabla1 = tabulate(lote_actual_tabla, headers=headersA, tablefmt="fancy_grid")

    # ----------------------- PROCESO DE EJECUCIÓN
    headersE = ["Id", "Ope", "TME", "TT", "TR"]
    if proceso_actual:  # Verifica si proceso_actual no está vacío
        tiempo_estimado = proceso_actual[0][3]
        tiempo_restante = tiempo_estimado - contTiempo
        proceso_actual_tabla = [proceso_actual[0][0], proceso_actual[0][1], tiempo_estimado, contTiempo, tiempo_restante]
    else:
        # Si proceso_actual está vacío, establece los valores en blanco
        proceso_actual_tabla = ["", "", "", "", ""]

    # Transponer los datos para mostrarlos en forma vertical
    proceso_actual_tabla_transpuesta = [[header, value] for header, value in zip(headersE, proceso_actual_tabla)]
    tabla2 = tabulate(proceso_actual_tabla_transpuesta,  tablefmt="fancy_grid")

    # ----------------------------------- Procesos terminados
    headersT = ["ID", "Ope", "Res"]
    procesos_terminados_tabla = [[terminado[0], terminado[1], terminado[2]] for terminado in procesos_terminados]
    tabla3 = tabulate(procesos_terminados_tabla, headers=headersT, tablefmt="fancy_grid")

    # ------------------ PARA MOSTRAR EN HORIZONTAL
    # Dividir cada tabla en líneas
    lineas1 = tabla1.splitlines()
    lineas2 = tabla2.splitlines()
    lineas3 = tabla3.splitlines()

    # Determinar el número máximo de líneas entre las tres tablas
    max_lines = max(len(lineas1), len(lineas2), len(lineas3))

    # Rellenar las tablas más cortas con líneas en blanco si es necesario
    lineas1 += ['\t\t'] * (max_lines - len(lineas1))
    lineas2 += ['\t'] * (max_lines - len(lineas2))
    lineas3 += [''] * (max_lines - len(lineas3))

    # Alinear horizontalmente las líneas de las tablas
    tabla_final = ''
    for i in range(max_lines):
        fila = lineas1[i] + "\t\t" + lineas2[i] + "\t\t\t" + lineas3[i]
        tabla_final += fila + '\n'

    print(tabla_final)
    print("Contador: ", contadorGeneral)


def main():
    global contProcess
    global procesosMax
    global lote_actual
    global proceso_actual
    global procesos_terminados
    global contTiempo
    global contLote
    global contPendiente
    global contadorGeneral

    procesosMax = 5
    contProcess = 0
    contLote=0
    contadorGeneral = 0

    lotes_de_procesos()
    procesos_terminados = []

    contTotal = numProcess // 5
    residuo = numProcess % 5
    if residuo != 0:
        contTotal += 1
    contPendiente = contTotal

    while contProcess != numProcess:

        contPendiente -= 1
        lote_actual = []
        proceso_actual = []
        
        contLote += 1

        for _ in range(procesosMax):
            if not procesos_pendientes:
                break       #rompe el programa

            proceso = procesos_pendientes.pop(0)
            lote_actual.append(proceso)

        while len(lote_actual) != 0:
            #contTiempo=0
            contTiempo = lote_actual[0][4]
            actual = lote_actual.pop(0)
            proceso_actual.append(actual)
                
            while True:
                os.system("cls")
                contTiempo += 1
                contadorGeneral += 1                    
                imprimir()
                t.sleep(1)
                intoTecla()

                if tiempo_restante == 0:
                    t.sleep(1)
                    finalizado = proceso_actual.pop(0)
                    procesos_terminados.append(finalizado)
                    contProcess += 1
                    break
                
                if tecla == 'i':
                    interrumpido = proceso_actual.pop(0)
                    interrumpido[4] = contTiempo
                    lote_actual.append(interrumpido)
                    break
                    
                elif tecla == 'e':
                    error = proceso_actual.pop(0)
                    error[2] = 'Error'
                    procesos_terminados.append(error)
                    contProcess += 1
                    break

        if len(procesos_terminados) != len(lote_actual):
            a = "---"
            procesos_terminados.append(a)
    
    os.system("cls")
    imprimir()
    mv.getch()

main()