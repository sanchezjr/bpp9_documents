import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def leerDatos():
    try:
        with open('finanzas2020.csv') as f:
            reader = csv.reader(f)
            #next(reader)
            for fila in reader:
                finanzas.append(fila[0].split("\t"))

    except:
        print("No se encuentra el documento especificado o no tiene sus 12 columnas")

def verificarDatos():

    try:
        #Validamos que todos los datos son correctos
        for fila in range(1, len(finanzas)):
            for columna in range(len(finanzas[0])):
                if finanzas[fila][columna][0] == "-":
                    if finanzas[fila][columna][1:].isdigit() == False:
                        finanzas[fila][columna] = "0"
                else:
                    if finanzas[fila][columna][1:].isdigit() == False:
                        finanzas[fila][columna] = "0"


        # Agregamos los meses a una lista
        for i in range(12):
            meses.append(finanzas[0][i])

        # Registramos los gastos de todos los meses
        for fila in range(1, len(finanzas)):
            for columna in range(len(finanzas[0])):
                if int(finanzas[fila][columna]) < 0:
                    gastos[columna] += int(finanzas[fila][columna])
                if int(finanzas[fila][columna]) >= 0:
                    ingresos[columna] += int(finanzas[fila][columna])
        # Mostramos los datos
        for fila in finanzas:
            for columna in fila:
                print(columna, end=" ")
            print()

        masGastos = gastos[0]
        menosGastos = gastos[0]
        mesMenos = meses[0]
        mesMas = meses[0]
        for i in range(len(gastos)):
            if abs(gastos[i]) > abs(masGastos):
                masGastos = abs(gastos[i])
                mesMas = meses[i]
            if abs(gastos[i]) < abs(menosGastos):
                menosGastos = abs(gastos[i])
                mesMenos = meses[i]
        mediaGastos = round(statistics.mean(gastos), 3)
        gastoTotal = abs(sum(gastos))
        ingresoTotal = sum(ingresos)
        print()
        print("El mes que se ha gastado mas es: ", mesMas)
        print("El mes que se ha ahorrado mas es: ", mesMenos)
        print("La media de todos los gastos del año es: ", mediaGastos)
        print("Los gastos totales en todo el año suma: ", gastoTotal)
        print("El total de ingresos del año es: ", ingresoTotal)

    except:
        print("Algo fallo")

finanzas = []
meses = []
gastos = [int() for i in range(12)]
ingresos = [int() for i in range(12)]

leerDatos()
verificarDatos()
