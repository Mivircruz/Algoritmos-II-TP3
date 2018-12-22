# !/usr/bin/python3

import heapq
import math
import grafo as g
import vertice as v

def obtener_parametros(linea):

	parametros = []
	sep = " "
	parametros.append(linea.split(","))
	aux = parametros[0].split(" ")

	if len(aux) > 2:
		aux[1] = sep.join((aux[1], aux[2]))

	parametros.insert(0, aux[1])

	return parametros


def recorrido_dfs(grafo, v, visitados, padres, orden):
	visitados.add(v)
	for w in grafo.obtener_adyacentes(v):
		if w not in visitados:
			padres[w] = v
			orden[w] = orden[v] + 1
			recorrido_dfs(grafo, w, visitados, padres, orden)


def dfs(grafo, origen):
	visitados = set()
	padres = {}
	orden = {}
	padres[origen] = None
	orden[origen] = 0
	recorrido_dfs(grafo, origen, visitados, padres, orden)
	return padres, orden


def bfs(grafo, origen):
	visitados = set()
	padres = {}
	orden = {}
	cola = []
	visitados.add(origen)
	padres[origen] = None
	orden[origen] = 0
	cola.append(origen)

	while len(cola) != 0:
		v = cola.pop(0)
		for w in grafo.obtener_adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				padres[w] = v
				orden[w] = orden[v] + 1
				cola.append(w)

	return padres, orden

def obtener_peso_minimo(grafo, aeropuerto_origen, destino, modo):
	mejor_peso = float('inf')
	mejor_aeropuerto = None

	for aeropuerto_destino in grafo.obtener_aeropuertos(destino):

		if modo == "barato":
			peso_actual = grafo.obtener_precio(aeropuerto_origen,aeropuerto_destino)
		elif modo == "rapido":
			peso_actual = grafo.obtener_tiempo(aeropuerto_origen,aeropuerto_destino)
		else:
			peso_actual = grafo.obtener_cant_vuelos(aeropuerto_origen,aeropuerto_destino)

		if peso_actual < mejor_peso:
			mejor_peso = peso_actual
			mejor_aeropuerto = aeropuerto_destino

	return mejor_aeropuerto


def camino_minimo(grafo, aeropuerto_origen, destino, modo):

	distancia = {}
	padres = {}
	visitados = set()
	heap = []

	for vertice in grafo.obtener_todos_vertices().keys():
		for aeropuerto in grafo.obtener_aeropuertos(grafo.obtener_ciudad(vertice)):
			distancia[aeropuerto] = float('inf')

	distancia[aeropuerto_origen] = 0
	padres[aeropuerto_origen] = None
	visitados.add(grafo.obtener_ciudad(aeropuerto_origen))
	heapq.heappush(heap, (distancia[aeropuerto_origen], aeropuerto_origen))

	while heap:

		vertice = heapq.heappop(heap)
		visitados.add(grafo.obtener_ciudad(vertice[1]))

		if grafo.obtener_ciudad(vertice[1]) == destino:
			return padres, distancia

		for adyacente in grafo.obtener_adyacentes(vertice[1]).keys():
			ciudad_adyacente = grafo.obtener_ciudad(adyacente)
			if ciudad_adyacente not in visitados:
				adyacente = obtener_peso_minimo(grafo, vertice[1], ciudad_adyacente, modo)
				if modo == "barato":
					peso = grafo.obtener_precio(vertice[1], adyacente)
				else:
					peso = grafo.obtener_tiempo(vertice[1], adyacente)

				if vertice[0] + peso < distancia[adyacente]:
					distancia[adyacente] = vertice[0] + peso
					padres[adyacente] = vertice[1]
					heapq.heappush(heap, (distancia[adyacente], adyacente))

	return padres, distancia

def prim(grafo, aeropuerto_origen, modo):

	visitados = set()
	visitados.add(aeropuerto_origen)
	heap = []
	arbol = g.Grafo()
	vertice_actual = grafo.obtener_vertice(aeropuerto_origen)

	for adyacente in vertice_actual.obtener_adyacentes().keys():
		if modo == "barato":
			peso_arista = grafo.obtener_precio(grafo.obtener_codigo(aeropuerto_origen), adyacente)
		else:
			peso_arista = grafo.obtener_tiempo(grafo.obtener_codigo(aeropuerto_origen), adyacente)

		heapq.heappush(heap, (peso_arista, adyacente, aeropuerto_origen))


#POR QUÉ VALUES SI USAS EL VERTICE COMO CLASE PARA LLAMAR A LAS PRIMITIVAS???

	for v in grafo.obtener_todos_vertices().values():
		arbol.agregar_vertice(v.obtener_ciudad(), v.obtener_codigo(), v.obtener_latitud(), v.obtener_longitud())

	while heap:
		v = heapq.heappop(heap)
		if grafo.obtener_ciudad(v[1]) in visitados:
			continue

		if modo == "barato":
			arbol.agregar_arista(v[1], v[2], 0, v[0], 0)
		else:
			arbol.agregar_arista(v[1], v[2], v[0], 0, 0)

		visitados.add(grafo.obtener_ciudad(v[1]))

		vertice_actual = grafo.obtener_vertice(v[1])

		for key in vertice_actual.obtener_adyacentes().keys():
			ciudad_adyacente = grafo.obtener_ciudad(key)

			if ciudad_adyacente not in visitados:

				key = obtener_peso_minimo(grafo, v[1], ciudad_adyacente, modo)
				if modo == "barato":
					a_guardar = grafo.obtener_precio(v[1], key)
				else:
					a_guardar = grafo.obtener_tiempo(v[1], key)

				heapq.heappush(heap, (a_guardar, key, v[1]))

	return arbol


def recorrido_vacaciones(grafo, v, padres, contador, destino, n):

	ciudad_actual = grafo.obtener_ciudad(v)

	if contador == n and ciudad_actual == destino:
		return True

	if contador == n and ciudad_actual != destino:
		return False

	for adyacente in grafo.obtener_adyacentes(v).keys():
		padres[adyacente] = v
		contador += 1
		if recorrido_vacaciones(grafo, adyacente, padres, contador, destino, n):
			return True
	padres.pop(v)
	return False


def ordenar_vertices(dist):
	heap = []
	dist_ = {}

	for clave, valor in dist.items():
		heapq.heappush(heap, (valor, clave))

	return heap


def centralidad(grafo):
	cent = {}

	for key in grafo.obtener_todos_vertices().keys():
		cent[key] = 0

	for key1 in grafo.obtener_todos_vertices().keys():
		padres, dist = bfs(grafo, key1)
		cent_aux = {}
		for key2 in grafo.obtener_todos_vertices().keys():
			cent_aux[key2] = 0

		# Filtra infinitos
		for a in dist:
			if type(dist) is float:
				if math.isinf(a):
					dist.pop(a)

		# HCER FUNCION ORDENAR_VERTICES!!!!!
		vertices_ordenados = ordenar_vertices(dist)

		for w in vertices_ordenados:
			if w[1] == key1:
				continue

			cent_aux[padres[w[1]]] += 1
			cent_aux[padres[w[1]]] += cent_aux[w[1]]

		for w in grafo.obtener_todos_vertices().keys():
			if w == key1:
				continue

			cent[w] += cent_aux[w]

	return cent
