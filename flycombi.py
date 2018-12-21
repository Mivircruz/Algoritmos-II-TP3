#!/usr/bin/python3

import sys
import comandos
import grafo as g

def conexiones(aeropuertos, vuelos):

    grafo = g.Grafo()

    for linea in aeropuertos:

        info_aeropuerto = linea.split(",")
        grafo.agregar_vertice(info_aeropuerto[0], info_aeropuerto[1], info_aeropuerto[2], info_aeropuerto[3])

    for linea in vuelos:
        info_vuelo = linea.split(",")
        grafo.agregar_arista(info_vuelo[0], info_vuelo[1], info_vuelo[2], info_vuelo[3], info_vuelo[4])

    return grafo


def main():

    aeropuerto = open(sys.argv[1], "r")
    vuelos = open(sys.argv[2], "r")

    grafo = conexiones(aeropuerto, vuelos)

   # sys.argv[1].close()
   # sys.argv[2].close()

    linea = sys.stdin.readline().rstrip('\n')
    parametros = linea.split(",")
    a_ejecutar = parametros[0].split(" ")
    aux = " "

    if a_ejecutar[0] not in comandos.comandos:
        print("Error")
        return

    if a_ejecutar[0] == comandos.comandos[5]:
        comandos.listar_operaciones()

    elif a_ejecutar[0] == comandos.comandos[0]:
        if len(a_ejecutar) > 2:
            a_ejecutar[1] = aux.join((a_ejecutar[1], a_ejecutar[2]))
        comandos.camino_mas(a_ejecutar[1], parametros[1], parametros[2], grafo)

    elif a_ejecutar[0] == comandos.comandos[1]:
        if len(a_ejecutar) > 2:
            a_ejecutar[1] = aux.join((a_ejecutar[1], a_ejecutar[2]))

        comandos.camino_escalas(grafo, a_ejecutar[1], parametros[1])

    elif a_ejecutar[0] == comandos.comandos[2]:
        if len(a_ejecutar) > 2:
            a_ejecutar[1] = aux.join((a_ejecutar[1], a_ejecutar[2]))
        comandos.centralidad_aprox(grafo, a_ejecutar[1])

    elif a_ejecutar[0] == comandos.comandos[4]:
        if len(a_ejecutar) > 2:
            a_ejecutar[1] = aux.join((a_ejecutar[1], a_ejecutar[2]))
        comandos.vacaciones(grafo, a_ejecutar[1], a_ejecutar[2])
    else:
        if len(a_ejecutar) > 2:
            a_ejecutar[1] = aux.join((a_ejecutar[1], a_ejecutar[2]))
        comandos.recorrer_mundo_aprox(grafo, a_ejecutar[1])



main()
