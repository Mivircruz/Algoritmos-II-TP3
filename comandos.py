# !/usr/bin/python3

import funciones
import math


def camino_mas(grafo, linea):

    parametros = funciones.obtener_parametros(linea)

    modo = parametros[0]
    origen = parametros[1]
    destino = parametros[2]
    aeropuertos = grafo.obtener_aeropuertos(origen)
    peso_min = float('inf')
    padres_final = {}
    destino_final = None
    indice = 0

    for i in range(0, len(aeropuertos)):
        padres, dist, peso, destino = funciones.camino_minimo(grafo, aeropuertos[i], destino, modo)
        if peso < peso_min:
            padres_final = padres
            peso_min = peso
            destino_final = destino
            indice = i

    lista = []
    lista.append(destino_final)
    v = lista[0]

    while v != aeropuertos[indice]:
        v = padres_final[v]
        lista.append(v)


    while lista:
        if len(lista) != 1:
            print lista.pop()+"->",

        else:
            print lista.pop()



def camino_escalas(grafo, linea):

    parametros = funciones.obtener_parametros(linea)

    origen = parametros[0]
    destino = parametros[1]
    arreglo_ordenes = []
    arreglo_padres = []
    arreglo_origenes = []
    i = 0
    mejor_orden = float('inf')

    for aeropuerto in grafo.obtener_aeropuertos(origen):
        padres, orden = funciones.bfs(grafo, aeropuerto)
        arreglo_ordenes[i] = orden
        arreglo_padres[i] = padres
        arreglo_origenes[i] = aeropuerto
        i+=1

    for aeropuerto in grafo.obtener_aeropuertos(destino):
        i = 0
        while aeropuerto not in arreglo_padres[i]:
            i+=1
        if arreglo_ordenes[i] < mejor_orden:
            mejor_orden = arreglo_ordenes[i]
            mejores_padres = arreglo_padres[i]
            codigo_destino = aeropuerto
            codigo_origen = arreglo_origenes[i]

    v = mejores_padres[codigo_destino]
    lista = []
    lista.append(codigo_destino)

    while v != codigo_origen:
        lista.append(v)
        v = mejores_padres[v]

    if v != mejores_padres[codigo_destino]:
        lista.append(v)

    while lista:
        if len(lista) == 1:
            print(lista.pop())

        else:
            print(lista.pop(), "->")


def centralidad_aprox(grafo, linea):

    parametros = funciones.obtener_parametros(linea)

    cent = funciones.centralidad(grafo)
    vertices = funciones.ordenar_vertices(cent)

    for i in range(0, int(parametros[0])):
        if i != int(parametros[0])-1:
            print vertices.pop()[0]+",",
        else:
            print vertices.pop()[0]


def recorrer_mundo_aprox(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    origen = parametros[0]

    lugares_del_mundo = grafo.obtener_todas_ciudades()
    tiempo = float('inf')
    actual = origen
    visitados = []
    costo = 0

    while lugares_del_mundo:

        codigo_actual = grafo.obtener_codigo(actual)
        visitados.append(codigo_actual)
        lugares_del_mundo.pop(actual)

        for ady in grafo.obtener_adyacentes(codigo_actual).keys():

            ady = funciones.obtener_peso_minimo(grafo, codigo_actual, ady, "rapido")
            ciudad_ady = grafo.obtener_ciudad(ady)
            if ciudad_ady == actual:
                continue

            tiempo_ady = grafo.obtener_tiempo(codigo_actual, ady)
            if  tiempo_ady < tiempo:
                tiempo = tiempo_ady
                actual = ciudad_ady
        costo += tiempo

    for i in range(0, len(visitados)):
        print(visitados[i])
        if i < len(visitados) - 1:
            print("->")
    print("Costo: ", costo)


def vacaciones(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    origen = parametros[0]
    n = parametros[1]

    padres = {}

    for aeropuerto in grafo.obtener_aeropuertos(origen):
        padres[aeropuerto] = None
        if funciones.recorrido_vacaciones(grafo, aeropuerto, padres, 0, origen, n):
            break

# for key, values in padres:
#    print(values)
#   print("->")

comandos = {
    "camino_mas": camino_mas,
    "camino_escalas": camino_escalas,
    "centralidad_aprox": centralidad_aprox,
    "recorrer_mundo_aprox": recorrer_mundo_aprox,
    "vacaciones": vacaciones
}
