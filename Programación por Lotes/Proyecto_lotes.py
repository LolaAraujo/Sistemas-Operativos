"""
CreatMed on Wed Aug 30 21:05:52 2023

@author: Lola&Aldo
"""
import os
from tabulate import tabulate
import time as t

IDs = []

def cantidad_procesos():
    global numProcess
    while True:
        try:
            numProcess = int(input("\nDame un número de procesos (Máximo 30): "))
            if 0 < numProcess <= 30: #Esto luego lo eliminamos, solo es para poner un límitMe de procesos
                break
            else:
                print("\nEl número de procesos debe estar entre 1 y 30.\n")
        except ValueError:
            print("\nNúmero Inválido.\n")


def ID():
    global id

    while True:
        try:
            id = int(input("\nDame un ID: "))
            if 0 < id:
                if id in IDs: #Comprobación de ID
                    print("\nID ya existente\n")
                else:
                    IDs.append(id)
                    break
            else:
                print("\nPor favor, ingresa un número válido.\n")
        except ValueError:
            print("\nPor favor, ingresa un número válido.\n")


def nombre():
    global user

    while True:
        user = input("\nDame tu nombre: ")

        if user.strip(): #verificación de que la variable no estMe vacía
            break

        else:
            print("\nPor favor, ingresa un nombre válido.\n")


def isOperador():
    global resultado
    global operaciones

    #Recursivo y excepciones
    while True:
        while True:
            try:
                num1 = int(input("\nIngresa un número: "))
                num2 = int(input("\nIngresa otro número: "))
                break
            except ValueError:
                print("Solo se admiten números!!")

        if num1 < 0 or num2 < 0:
            print("Solo se aceptan numeros mayores a cero")

        else:
            try:
                print("\nElige una operación:\n[1]Suma\n[2]Resta\n[3]Multiplicación\n[4]División\n[5]Residuo\n[6]Potencia")
                opc = int(input(": "))

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
                    if num1 > 0 or num2 > 0:
                        operador = '/'
                        resultado = num1/num2
                        break
                    else:
                        print("No se aceptan valores negativos o iguales a cero")

                elif opc == 5:
                    if num1 > 0 or num2 > 0:
                        operador = '%'
                        resultado = num1%num2
                        break
                    else:
                        print("No se aceptan valores negativos o iguales a cero")

                elif opc == 6:
                    if num1 > 0 and num2 > 0:
                        operador = '**'
                        resultado = num1**num2
                        break
                    else:
                        print("Cero no se puede elevar a cero")

                else:
                    print('\nERROR!!')

            except ValueError:
                print('\nERROR!!')

    operaciones = f"{num1}{operador}{num2}"


def tiempo_estimado():
    global TME
    while True:
        try:
            TME = int(input("\nDame el tiempo estimado: "))

            if 0 < TME <= 20: #Esto luego lo eliminamos, solo es para poner un límitMe de procesos
                break
            else:
                print("\nEl tiempo estimado debe ser un número mayor que 1.\n")
        except ValueError:
            print("\nPor favor, ingresa un número válido.\n")


def lotes_de_procesos():
    global info
    global procesos_pendientes
    global totalProces
    info = []
    procesos_pendientes=[]
    
    proceso = 1
    os.system("cls")
    cantidad_procesos()
    totalProces = numProcess

    while totalProces != 0:
        os.system("cls")
        print("Proceso ", proceso, " de ", numProcess, ".\n")
        ID()
        nombre()
        isOperador()
        tiempo_estimado()
        info = [id,user,operaciones,resultado,TME]
        procesos_pendientes.append(info)
        os.system("cls")
        totalProces -= 1
        proceso += 1


def imprimir():
    global tiempo_restante
    # -------------------------- Lotes Actuales
    print("\nNo. Lotes Pendientes: ", contPendiente)
    print("\nLote Actual: ", contLote, "\t Proceso en Ejecución \t\tProcesos Terminados")

    headersA = ["ID", "TME"]
    lote_actual_tabla = [[lista[0], lista[4]] for lista in lote_actual]
    tabla1 = tabulate(lote_actual_tabla, headers=headersA, tablefmt="double_outline")

    # ----------------------- PROCESO DE EJECUCIÓN
    headersE = ["Nom", "Id", "Ope", "TME", "TT", "TR"]
    if proceso_actual:  # Verifica si proceso_actual no está vacío
        tiempo_estimado = proceso_actual[0][4]
        tiempo_restante = tiempo_estimado - contTiempo
        proceso_actual_tabla = [proceso_actual[0][1], proceso_actual[0][0], proceso_actual[0][2], tiempo_estimado, contTiempo, tiempo_restante]
    else:
        # Si proceso_actual está vacío, establece los valores en blanco
        proceso_actual_tabla = ["", "", "", "", "", ""]
        
    # Transponer los datos para mostrarlos en forma vertical
    proceso_actual_tabla_transpuesta = [[header, value] for header, value in zip(headersE, proceso_actual_tabla)]
    tabla2 = tabulate(proceso_actual_tabla_transpuesta,  tablefmt="double_outline")

    # ----------------------------------- Procesos terminados
    headersT = ["ID", "Ope", "Res"]
    procesos_terminados_tabla = [[terminado[0], terminado[2], terminado[3]] for terminado in procesos_terminados]
    tabla3 = tabulate(procesos_terminados_tabla, headers=headersT, tablefmt="double_outline")

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
        fila = lineas1[i] + "\t    " + lineas2[i] + " \t\t   " + lineas3[i]
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

    contTotal = numProcess // 5
    residuo = numProcess % 5
    if residuo != 0:
        contTotal += 1
    contPendiente = contTotal
    
    while contProcess != numProcess:
        
        contPendiente -= 1
        lote_actual = []
        proceso_actual = []
        procesos_terminados = []
        contLote += 1

        for _ in range(procesosMax):
            if not procesos_pendientes:
                break       #rompe el programa

            proceso = procesos_pendientes.pop(0)
            lote_actual.append(proceso)

        while len(lote_actual) != 0:
            contTiempo = 0

            actual = lote_actual.pop(0)
            proceso_actual.append(actual)
            
            while True:
                os.system("cls")
                contTiempo += 1
                contadorGeneral += 1
                imprimir()
                t.sleep(1)
                
                if tiempo_restante == 0:
                    t.sleep(1)
                    break
                
            finalizado = proceso_actual.pop(0)
            procesos_terminados.append(finalizado)
            contProcess += 1
            
        if len(procesos_terminados) != len(lote_actual):
            os.system("cls")
            imprimir()
            t.sleep(2)
                            
main()
