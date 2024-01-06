"""
CreatMed on Wed Sep 19 21:05:52 2023

@author: Lola&Aldo  versión 3
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

def procesos():
    global info
    global procesos_pendientes
    global totalProces
    global contTiempo
    global Tr
    
    contTiempo = 0
    Tr = 0
    tiempoBloq = 0
    tiempoLlegada = 0
    tiempoFinal=0
    tiempoServicio=0
    tiempoEspera=0
    tiempoRetorno=0
    tiempoRespuesta=0
    bandera=0
    tiempoTotalBloqueado=0
    info = []
    procesos_pendientes=[]

    os.system("cls")
    cantidad_procesos()
    totalProces = numProcess

    while totalProces != 0:
        os.system("cls")
        ID()
        isOperador()
        tiempo_estimado()
        info = [id, operaciones, resultado, TME, contTiempo, Tr, tiempoBloq, tiempoLlegada, tiempoServicio, tiempoEspera, tiempoRespuesta, tiempoRetorno, tiempoFinal, 
                bandera, tiempoTotalBloqueado]
        procesos_pendientes.append(info)
        os.system("cls")
        totalProces -= 1   

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
    # -------------------------- Lotes Actuales
    print("\nNo. Procesos Nuevos: ", contPendiente)
    print("\nProcesos Listos: ", contListos, "\t\tProceso en Ejecución \t\tProcesos Terminados")

    headersA = ["ID", "TME", "TT"]
    actual_tabla = [[lista[0], lista[3], lista[4]] for lista in procesos_actuales]
    tabla1 = tabulate(actual_tabla, headers=headersA, tablefmt="fancy_grid")

    # ----------------------- PROCESO DE EJECUCIÓN
    headersE = ["Id", "Ope", "TME", "TT", "TR"]
    if proceso_ejecucion:  # Verifica si proceso_enEjecucion no está vacío
        proceso_ejecucion[0][5] = proceso_ejecucion[0][3] - proceso_ejecucion[0][4]
        proceso_actual_tabla = [proceso_ejecucion[0][0], proceso_ejecucion[0][1], proceso_ejecucion[0][3], proceso_ejecucion[0][4], proceso_ejecucion[0][5]]
    else:
        # Si proceso_enEjecucion está vacío, establece los valores en blanco
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
    
    #TABLA DE BLOQUEADOS
    print("\n\nBloqueados")
    headersB = ["ID", "TB"]
    proceso_bloq = [[lista[0], lista[6]] for lista in procesos_bloqueados]
    print(tabulate(proceso_bloq, headers=headersB, tablefmt="double_outline"))

    print("\nContador: ", contadorGeneral)
    
def impresion_final():
    print("\n\n\nProcesos")
    headersB = ["ID", "Ope", "Res", "TME", "TT", "TR", "TB", "TLl", "TS", "TE", "TRes", "TRet", "TF"]
    procesoGen = [[dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[14], dato[7], dato[8], dato[9], dato[10], dato[11], dato[12]] for dato in procesos_terminados]
    print(tabulate(procesoGen, headers=headersB, tablefmt="double_outline"))


def main():
    global contProcess
    global procesosMax
    global procesos_actuales
    global proceso_ejecucion
    global procesos_terminados
    global contListos
    global contPendiente
    global contadorGeneral
    global procesos_bloqueados


    procesosMax = 5
    contProcess = 0
    contListos=0
    contadorGeneral = 0

    procesos()
    procesos_terminados = []
    procesos_actuales = []
    procesos_bloqueados = []
    proceso_ejecucion = []
    

    while contProcess != numProcess:
        
        long1 = len(procesos_actuales)
        long2 = len(proceso_ejecucion)
        long3 = len(procesos_bloqueados)
        long = long1+long2+long3

        for _ in range(procesosMax-long):
            if not procesos_pendientes:
                break       #rompe el programa

            proceso = procesos_pendientes.pop(0)
            proceso[7] = contadorGeneral
            procesos_actuales.append(proceso)
            
            
        if procesos_actuales: 
            actual = procesos_actuales.pop(0)
            if actual[13] == 0: 
                    actual[13] = 1
                    contResp = contadorGeneral-actual[7]
                    actual[10] = contResp
            proceso_ejecucion.append(actual)
            
        while True:
            contPendiente = len(procesos_pendientes)
            contListos = len(procesos_actuales)
            os.system("cls")
            if proceso_ejecucion:
                proceso_ejecucion[0][4] += 1                  
            imprimir()
            contadorGeneral += 1 
            t.sleep(1)
            intoTecla()
            
            for bloqueados in procesos_bloqueados: 
                bloqueado = bloqueados[6]
                
                if bloqueado < 8:
                    bloqueados[6] += 1
                    bloqueados[14] +=  1
                    
                elif bloqueado == 8:
                    bloqueados[6] = 0
                    bloqueados[14] +=  1
                    desbloqueado = procesos_bloqueados.pop(0)
                    procesos_actuales.append(desbloqueado)
                    if not proceso_ejecucion:
                        actual = procesos_actuales.pop(0)
                        proceso_ejecucion.append(actual)
                    
            if proceso_ejecucion:
                if proceso_ejecucion[0][5] == 0: 
                    t.sleep(1)
                    finalizado = proceso_ejecucion.pop(0)
                    finalizado[12] = contadorGeneral
                    finalizado[8] = finalizado[4]
                    finalizado[11] = finalizado[12]-finalizado[7]
                    finalizado[9] = finalizado[11]-finalizado[8]
                    procesos_terminados.append(finalizado)
                    contProcess += 1
                    break
                
            if tecla == 'i':
                if proceso_ejecucion:
                    interrumpido = proceso_ejecucion.pop(0)
                    interrumpido[6] = 1
                    procesos_bloqueados.append(interrumpido)
                break
                
            elif tecla == 'e':
                if proceso_ejecucion:
                    error = proceso_ejecucion.pop(0)
                    error[2] = 'Error'
                    error[8] = error[4]
                    error[12] = contadorGeneral
                    error[11] = error[12]-error[7]
                    error[9] = error[11]-error[8]
                    procesos_terminados.append(error)
                    contProcess += 1
                break
        
    os.system("cls")
    imprimir()
    t.sleep(1)
    os.system("cls")
    impresion_final()
    #print("\nContador General:",contadorGeneral)
    mv.getch()

main()