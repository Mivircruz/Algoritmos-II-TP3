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

	return padres, orden

def camino_mas_rapido(grafo, origen, destino):

	if not Grafo.pertenece(grafo, origen) or not Grafo.pertenece(grafo,origen):
		return False

	distancia = {}
	padres = {}
	visitados = set()

	for key,values in grafo.obtener_todos_vertices(grafo):
		distancia[key] = math.inf

	distancia[origen] = 0
	padres[origen] = None
	visitados.add(origen)
	heap_tiempo = [(dist[origen], origen)]

	while heap_tiempo:
		v = heapq.heappop(heap_tiempo)
		visitados.add(v[1])
		if v[1] == destino:
			return padres, distancia

		vertice_actual = grafo.obtener_vertice(grafo, v[1])

		for key, value in vertice.obener_adyacentes(vertice_actual):

			if key not in visitados:
				if distancia[v[1]] + Vertice.obtener_tiempo(vertice_actual, key) < distancia[key]:
					distancia[key] = distancia[v[1]] + vertice.obtener_tiempo(vertice_actual, key)
					padres[key] = v[1]
					heapq.heappush(heap_tiempo, (dist[key], key))

	return padres

def camino_mas_barato(grafo, origen, destino):

	visitados = set()
	visitados.append(origen)
	heap_precios = []
	camino = []


	for key, value in vertice.obtener_adyacentes(grafo.obtener_vertice(grafo, origen)):
		heapq.heappush(heap_precios, (vertice.obtener_precio(grafo.obtener_vertice(grafo, origen), key))

	while heap_precios:
		v = heapq.heappop(heap_precios)
		camino.append(v[1])
		if v[1] in visitados:
			continue
		visitados.append(v[1])

		vertice_actual = grafo.obtener_vertice(grafo, v[1])

		for key,values in vertice.obtener_adyacentes(vertice_actual):

			if key not in visitados:
				heapq.heappush(heap_precios, (vertice.obtener_precio(grafo.obtener_vertice(grafo, v[1]), key)))

	return camino