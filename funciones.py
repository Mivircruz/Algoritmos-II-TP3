# !/usr/bin/python3

import heapq
import math
import grafo as g
import vertice as v


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


def camino_minimo(grafo, origen, destino, modo):

	distancia = {}
	padres = {}
	visitados = set()
	for key in grafo.obtener_todos_vertices():
		distancia[grafo.obtener_ciudad(key)] = float('inf')

	distancia[origen] = 0
	padres[origen] = None
	visitados.add(origen)
	heap_tiempo = []
	heapq.heappush(heap_tiempo, (distancia[origen], origen))

	while heap_tiempo:
		v = heapq.heappop(heap_tiempo)
		v_codigo = grafo.obtener_codigo(v[1])
		visitados.add(v_codigo)
		if v[1] == destino:
			return padres, distancia
		for key in grafo.obtener_adyacentes(v_codigo):
			if key not in visitados:
				if modo == "barato":
					peso = grafo.obtener_precio(v_codigo, key)
				elif modo == "rapido":
					peso = grafo.obtener_tiempo(v_codigo, key)
				else:
					peso = grafo.obtener_cant_vuelos(v_codigo, key)

				w_ciudad = grafo.obtener_ciudad(key)
				if distancia[v[1]] + peso < distancia[w_ciudad]:
					distancia[w_ciudad] = distancia[v[1]] + peso
					padres[key] = v_codigo
					heapq.heappush(heap_tiempo, (distancia[w_ciudad], key))

	return padres, distancia

def prim(grafo, origen, modo):

	visitados = set()
	visitados.add(origen)
	heap = []
	vertice_actual = grafo.obtener_vertice(grafo.obtener_codigo(origen))

	for key in vertice_actual.obtener_adyacentes().keys():
		if modo == "barato":
			a_guardar = grafo.obtener_precio(grafo.obtener_codigo(origen), key)
		else:
			a_guardar = grafo.obtener_tiempo(grafo.obtener_codigo(origen), key)

		heapq.heappush(heap, (a_guardar, key, grafo.obtener_codigo(origen)))

	arbol = g.Grafo()
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

			if grafo.obtener_ciudad(key) not in visitados:
				if modo == "barato":
					a_guardar = grafo.obtener_precio(v[1], key)
				else:
					a_guardar = grafo.obtener_tiempo(v[1], key)

				heapq.heappush(heap, (a_guardar, key, v[1]))



	return arbol


def recorrido_vacaciones(grafo, v, padres, contador, destino, n):
	if contador == n and v == destino:
		return True

	if contador == n and v != destino:
		return False

	codigo_v = grafo.obtener_codigo(v)
	for w in grafo.obtener_adyacentes(codigo_v).keys():
		ciudad_w = grafo.obtener_ciudad(w)
		padres[ciudad_w] = v
		contador += 1
		if recorrido_vacaciones(grafo, ciudad_w, padres, contador, destino, n) == True:
			return True
	padres.pop(codigo_v)
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
