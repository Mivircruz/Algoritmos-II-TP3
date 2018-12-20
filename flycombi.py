#!/usr/bin/python3

import sys
import comandos
import grafo as g

def conexiones(aeropuertos, vuelos):

    grafo = g.Grafo()

    for linea in aeropuertos:

        info_aeropuerto = linea.strip.split(",")
        grafo.agregar_vertice(grafo, info_aeropuerto[0], info_aeropuerto[1], info_aeropuerto[2], info_aeropuerto[3])

    for linea in vuelos:
        info_vuelo = linea.strip.split(",")
        grafo.agregar_arista(grafo, info_vuelo[0], info_vuelo[1], info_vuelo[2], info_vuelo[3], info_vuelo[4])

    return grafo


def main():

    archivos = sys.argv

    aeropuerto = open(archivos[1], "r")
    vuelos = open(archivos[2], "r")

    grafo = conexiones(aeropuerto, vuelos)

    archivo.close()
    archivo.close()


    for linea in sys.stdin:

        if linea[0] not in comandos:
            print("Error")

        if linea[0] == comandos[0]:
            comandos.camino_mas(linea[1], linea[2], linea[3], grafo)

        if linea[0] == comandos[1]:
            comandos.camino_escalas(linea[1], linea[2])

        if linea[0] == comandos[2]:
            comandos.centralidad_aprox(grafo, linea[1])

        else:
            comandos.recorrer_mundo_aprox(grafo, linea[1])






