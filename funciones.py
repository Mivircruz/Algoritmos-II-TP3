#!/usr/bin/python3

import heapq
import math
import grafo
import vertice

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

	return padres,orden

def camino_minimo(grafo, origen, destino):

	distancia = {}
	padres = {}
	visitados = set()

	for key in grafo.obtener_todos_vertices():
		distancia[key] = float('inf')

	distancia[origen] = 0
	padres[origen] = None
	visitados.add(origen)
	heap_tiempo = []
	heapq.heappush(heap_tiempo, (distancia[origen], origen))

	while heap_tiempo:
		v = heapq.heappop(heap_tiempo)
		visitados.add(v[1])
		if v[1] == destino:
			return padres, distancia

		for key in grafo.obtener_adyacentes(v[1]).keys():

			if key not in visitados:
				if (distancia[v[1]] + grafo.obtener_cant_vuelos(v[1], key)) < distancia[key]:
					distancia[key] = distancia[v[1]] + grafo.obtener_cant_vuelos(v[1], key)
					padres[key] = v[1]
					heapq.heappush(heap_tiempo, (distancia[key], key))

	return padres, distancia

def camino_mas_modo(grafo, origen, destino, modo):

	visitados = set()
	visitados.add(origen)
	heap = []
	camino = []


	for key in grafo.obtener_vertice(origen).obtener_adyacentes().keys():
		if modo == "barato":
			a_guardar =  grafo.obtener_precio(origen, key)
		else:
			a_guardar = grafo.obtener_tiempo(origen, key)

		heapq.heappush(heap, (a_guardar, key))

	while heap:
		v = heapq.heappop(heap)
		camino.append(v[1])

		if v[1] == destino:
			return camino

		if v[1] in visitados:
			continue
		visitados.add(v[1])

		vertice_actual = grafo.obtener_vertice(v[1])

		for key in vertice_actual.obtener_adyacentes().keys():

			if key not in visitados:
				if modo == "barato":
					a_guardar = grafo.obtener_precio(v[1], key)
				else:
					a_guardar = grafo.obtener_tiempo(v[1], key)

				heapq.heappush(heap, (a_guardar, key))

	return camino

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

		#Filtra infinitos
		for a in dist:
			if type(dist) is float:
				if math.isinf(a):
					dist.pop(a)


#HCER FUNCION ORDENAR_VERTICES!!!!!
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

def recorrido_vacaciones(grafo, v, visitados, padres, contador, destino, n):
	if contador == n and v == destino:
		return True

	if contador == n and v != destino:
		return False

	visitados.add(v)
	for w in grafo.obtener_adyacentes(grafo, v):
		if w not in visitados:
			padres[w] = v
			if recorrido(grafo, w, visitados, padres, contador + +, destino, n)
		return True
	visitados.remove(visitados, v)
	return False
