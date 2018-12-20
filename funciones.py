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
	heap_tiempo = [(distancia[origen], origen)]

	while heap_tiempo:
		v = heapq.heappop(heap_tiempo)
		visitados.add(v[1])
		if v[1] == destino:
			return padres

		for key in grafo.obtener_adyacentes(v[1]).keys():

			if key not in visitados:
				if (distancia[v[1]] + grafo.obtener_cant_vuelos(v[1], key)) < distancia[key]:
					distancia[key] = distancia[v[1]] + grafo.obtener_cant_vuelos(v[1], key)
					padres[key] = v[1]
					heapq.heappush(heap_tiempo, (distancia[key], key))

	return padres

def camino_mas_modo(grafo, origen, destino, modo):

	visitados = set()
	visitados.add(origen)
	heap = []
	camino = []


	for key in  vertice.obtener_adyacentes(grafo.obtener_vertice(origen)):
		if modo == "barato":
			a_guardar = grafo.obtener_precio(origen, key)
		else:
			a_guardar = grafo.obtener_tiempo(origen, key)
		heapq.heappush(heap, (a_guardar, key))

	while heap:
		v = heapq.heappop(heap)
		camino.append(v[1])

		ciudad = grafo.obtener_vertice(key).obtener_ciudad()
		if ciudad == destino:
			return camino

		if v[1] in visitados:
			continue
		visitados.add(v[1])

		vertice_actual = grafo.obtener_vertice(v[1])

		for key in vertice_actual.obtener_adyacentes():

			if key not in visitados:
				if modo == "barato":
					a_guardar = grafo.obtener_vertice(v[1]).obtener_precio()
				else:
					a_guardar = grafo.obtener_vertice(grafo, v[1]).obtener_tiempo()
				heapq.heappush(heap_precios, (a_guardar, key))

	return camino

def centralidad(grafo):

	cent = {}

	for key, values in grafo.obtener_todos_vertices(grafo):
		cent[key] = 0

	for key1, values in grafo.obtener_todos_vertices(grafo):
		padres_y_dist = bfs(grafo, vertice.obtener_ciudad(grafo.obtener_vertice(grafo, key1)))
		cent_aux = {}
		for key2, values in grafo.obtener_todos_vertices(grafo):
			cent_aux[key2] = 0

		#Filtra infinitos
		for key2, dist in padres_y_dist[1]:
			if dist == math.inf:
				padres_y_dist[1].pop(dist)


#HCER FUNCION ORDENAR_VERTICES!!!!!
		vertices_ordenados = ordenar_vertices(grafo, dist)

		for w in vertices_ordenados:
			cent_aux[padres_y_dist[0][w]] += 1
			cent_aux[padres_y_dist[0][w]] += cent_aux[w]

		for key2, values in grafo.obtener_todos_vertices(grafo):
			if key1 == key2:
				continue
			cent[key2] += cent_aux[key2]
	return cent

