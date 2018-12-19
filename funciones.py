#!/usr/bin/python3

import heapq
import grafo as g
import math

import grafo

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
	h_vertices = {}

	for key,values in Grafo.obtener_todos_vertices(grafo):
		distancia[key] = math.inf

	distancia[origen] = 0
	padres[origen] = None
	visitados.add(origen)

	heap_dist = [(origen, dist[origen])]
	h_vertices[origen] = Grafo.obtener_vertice(grafo, origen)

	while heap_dist:
		v = heapq.heappop(heap_dist)
		visitados.add(v[0])
		if v[0] == destino:
			return padres,distancia

		vertice_actual = Grafo.obtener_vertice(grafo, v[0])

		for key, value in Vertice.obener_adyacentes(vertice_actual):

			if key in visitados:
				if distancia[v[1]] + Vertice.obtener_tiempo(vertice_actual, key) > distancia[key]:
					continue
			distancia[key] = distancia[v[1]] + Vertice.obtener_tiempo(vertice_actual, key)
			padres[key] = v[0]
			heapq.heappush(heap_dist)

	return padres, distancia


