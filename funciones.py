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

	for key,values in grafo.obtener_todos_vertices(grafo):
		distancia[key] = math.inf

	distancia[origen] = 0
	padres[origen] = None
	visitados.add(origen)
	heap_tiempo = [(dist[origen], origen)]

	while heap_tiempo:
		v = heapq.heappop(heap_tiempo)
		visitados.add(v[1])
		ciudad = vertice.obtener_ciudad(grafo.obtener_vertice(grafo, key))
		if ciudad == destino:
			return padres

		vertice_actual = grafo.obtener_vertice(grafo, v[1])

		for key, value in vertice.obener_adyacentes(vertice_actual):

			if key not in visitados:
				if distancia[v[1]] + vertice.obtener_cant_vuelos(vertice_actual, key) < distancia[key]:
					distancia[key] = distancia[v[1]] + vertice.obtener_cant_vuelos(vertice_actual, key)
					padres[key] = v[1]
					heapq.heappush(heap_tiempo, (dist[key], key))

	return padres

def camino_mas_modo(grafo, origen, destino, modo):

	visitados = set()
	visitados.append(origen)
	heap = []
	camino = []


	for key, value in vertice.obtener_adyacentes(grafo.obtener_vertice(grafo, origen)):
		if modo == "barato"
			a_guardar =  vertice.obtener_precio(grafo.obtener_vertice(grafo, origen))
		else
			a_guardar = vertice.obtener_tiempo(grafo.obtener_vertice(grafo, origen))
		heapq.heappush(heap, (a_guardar, key))

	while heap_precios:
		v = heapq.heappop(heap_precios)
		camino.append(v[1])

		ciudad = vertice.obtener_ciudad(grafo.obtener_vertice(grafo, key))
		if ciudad == destino:
			return camino

		if v[1] in visitados:
			continue
		visitados.append(v[1])

		vertice_actual = grafo.obtener_vertice(grafo, v[1])

		for key,values in vertice.obtener_adyacentes(vertice_actual):

			if key not in visitados:
				if modo == "barato"
					a_guardar = vertice.obtener_precio(grafo.obtener_vertice(grafo, v[1]))
				else
					a_guardar = vertice.obtener_tiempo(grafo.obtener_vertice(grafo, v[1]))
				heapq.heappush(heap_precios, (a_guardar, key)))

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

