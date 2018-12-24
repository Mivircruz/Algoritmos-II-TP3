# !/usr/bin/python3

import funciones

def camino_mas(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    if len(parametros) != 3:
        return False
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
            print(lista.pop(), end=" ")
            print("->", end=" ")

        else:
            print(lista.pop())

    return True


def camino_escalas(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    if len(parametros) != 2:
        return False

    origen = parametros[0]
    destino = parametros[1]
    aeropuertos_origen = grafo.obtener_aeropuertos(origen)
    aeropuertos_destino = grafo.obtener_aeropuertos(destino)
    padres_final = {}
    indice = 0
    mejor_orden = float('inf')
    destino_final = None

    for i in range(0, len(aeropuertos_origen)):
        padres, orden = funciones.bfs(grafo, aeropuertos_origen[i])
        for k in range(0, len(aeropuertos_destino)):
            if orden[aeropuertos_destino[k]] < mejor_orden:
                padres_final = padres
                orden_final = orden
                indice = i
                destino_final = aeropuertos_destino[k]


    lista = []
    lista.append(destino_final)
    v = lista[0]

    while v != aeropuertos_origen[indice]:
        v = padres_final[v]
        lista.append(v)


    while lista:
        if len(lista) != 1:
            print(lista.pop(), end=" ")
            print("->", end=" ")

        else:
            print(lista.pop())

    return True


def centralidad_aprox(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    if len(parametros) != 1:
        return False

    cent = funciones.centralidad(grafo)
    vertices = funciones.ordenar_vertices(cent)

    for i in range(0, int(parametros[0])):
        if i != int(parametros[0])-1:
            print(vertices.pop()[0], ",", end=" ")
        else:
            print(vertices.pop()[0])

    return True


def recorrer_mundo_aprox(grafo, linea):

    parametros = funciones.obtener_parametros(linea)

    if len(parametros) != 1:
        return False

    origen = parametros[0]
    lugares = grafo.obtener_todas_ciudades()
    visitados = []
    costo = 0

    for aeropuerto in grafo.obtener_aeropuertos(origen):
        if funciones.recorrer_lugares(grafo, lugares, aeropuerto, costo, visitados):
            break
    
    for i in range(0, len(visitados)):
        if i < len(visitados) - 1:
            print(visitados[i], end=" ")
            print(" -> ", end=" ")
        else:
            print(visitados[i])
    print("Costo: ", costo)

    return True

def vacaciones(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    if len(parametros) != 2:
        return False

    origen = parametros[0]
    aeropuerto_origen = None
    visitados = []
    n = parametros[1]

    for aeropuerto in grafo.obtener_aeropuertos(origen):
        if funciones.recorrido_vacaciones(grafo, aeropuerto, aeropuerto, 0, int(n), visitados):
            aeropuerto_origen = aeropuerto
            break

    if len(visitados) == 0:
        print("No se encontro recorrido")
    else:
        for i in range(0,len(visitados)):
            print(visitados[i], end=" ")
            if i < len(visitados)-1:
                print("->", end=" ")
        print(aeropuerto_origen)

    return True

def nueva_aerolinea(grafo, linea):

    parametros = funciones.obtener_parametros(linea)
    if len(parametros) != 1:
        return False

    ruta = parametros[0]
    archivo = open(ruta, 'w')

#ORIGEN HARDCODEADO

    arbol, peso_total = funciones.prim(grafo,"SAN","barato")

    for aeropuerto in arbol.obtener_vertices().keys():
        archivo.write(aeropuerto + ',')

    archivo.close()
    print("Ok")
    return True


comandos = {
    "camino_mas": camino_mas,
    "camino_escalas": camino_escalas,
    "centralidad_aprox": centralidad_aprox,
    "recorrer_mundo_aprox": recorrer_mundo_aprox,
    "vacaciones": vacaciones
}
