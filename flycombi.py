#!/usr/bin/python3

import sys
import comandos

#Creo el grafo con los aeropuertos como vértices y los vuelos como las aristas

def conexiones(aeropuertos, vuelos):

    grafo = Grafo()

    for linea in aeropuertos:
        info_aeropuerto = linea.strip.split(",")
        grafo.agregar_vertice(grafo, info_aeropuerto[0], info_aeropuerto[1])

    for linea in vuelos:
        info_vuelo = linea.strip.split(",")
        grafo.agregar_arista(grafo, info_vuelo[0], info_vuelo[1], info_vuelo[2], info_vuelo[3], info_vuelo[4])

    return grafo

def main():

    archivos = sys.argv
    comando = input()

    aeropuerto =  open(archivos[1], "r")
    vuelos = open(archivos[2], "r")

    grafo = conexiones(aeropuerto, vuelos)

    if comando[0] in comandos:
        operacion_valida = comandos.comandos[comando](grafo, parametros)
    else:
        operacion_valida = false

    archivo.close()
    archivo.close()

    if operacion_valida == false:
        print("Error")

