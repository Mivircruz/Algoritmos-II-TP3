# !/usr/bin/python3

import funciones



def camino_mas(grafo, linea):

    parametros = obtener_parametros(linea)

    modo = parametros[0]
    origen = parametros[1]
    destino = parametros[2]


    padres, dist = funciones.camino_minimo(grafo, origen, destino, modo)
    lista = []
    lista.append(grafo.obtener_codigo(destino))
    v = lista[0]

    while v != origen:
        v = padres[v]
        lista.append(v)


    while lista:
        if len(lista) == 1:
            print(lista.pop())

        else:
            print(lista.pop(), "->")



def camino_escalas(grafo, linea):

    parametros = linea.split(",")

    origen = parametros[0]
    destino = parametros[1]

    padres, orden = funciones.bfs(grafo, grafo.obtener_codigo(origen))
    v = padres[grafo.obtener_codigo(destino)]
    lista = []
    lista.append(grafo.obtener_codigo(destino))

    while v != grafo.obtener_codigo(origen):
        lista.append(v)
        v = padres[v]

    if v != padres[grafo.obtener_codigo(destino)]:
        lista.append(v)

    while lista:
        if len(lista) == 1:
            print(lista.pop())

        else:
            print(lista.pop(), "->")


def centralidad_aprox(grafo, linea):

    cent = funciones.centralidad(grafo)
    vertices = funciones.ordenar_vertices(cent)

    for i in range(0, int(linea)):
        if i != int(linea)-1:
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

