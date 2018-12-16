#!/usr/bin/python3
import heap as h
import math
import grafo as g

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
