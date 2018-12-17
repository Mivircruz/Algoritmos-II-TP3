#!/usr/bin/python3

import sys
import comandos
import grafo as g



def main():

    archivos = sys.argv

    aeropuerto = open(archivos[1], "r")
    vuelos = open(archivos[2], "r")

    grafo = conexiones(aeropuerto, vuelos)

    archivo.close()
    archivo.close()


    for linea in sys.stdin:

        if linea[0] in comandos:
            operacion_valida = comandos.comandos[linea](grafo, parametros)
        else:
            operacion_valida = false



        if operacion_valida == false:
            print("Error")



def conexiones(aeropuertos, vuelos):

    grafo = g.Grafo()

    for linea in aeropuertos:

        info_aeropuerto = linea.split(",")
        grafo.agregar_vertice(info_aeropuerto[0], info_aeropuerto[1])

    for linea in vuelos:
        info_vuelo = linea.strip.split(",")
        grafo.agregar_arista(info_vuelo[0], info_vuelo[1], info_vuelo[2], info_vuelo[3], info_vuelo[4])

    return grafo


main()