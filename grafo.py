#!/usr/bin/python3


class Vertice(object):
	def __init__(self, clave, valor):
		self.clave = clave
		self.valor = valor
		self.conectado_a = {}
		
	def agregar_adyacente(self, adyacente, peso=0):
		self.conectado_a[adyacente.clave] = peso
		
	def obtener_adyacente(self):
		return self.conectado_a
	
	def obtener_peso(self, v):
		return self.conectado_a[v]
		
	def obtener_clave(self):
		return self.clave
		
	def obtener_valor(self):
		return self.valor
		

class Grafo(object):
	def __init__(self):
		self.vertices = []
		self.aristas = {}

	def agregar_vertice(self, v):
		if v not in self.vertices:
			self.vertices.append(v)
			return True
		
		else:
			return False
	
	def agregar_arista(self, v, w, peso=0):
		lista = [v.clave, w.clave]
		clave = ",".join(lista)
		if v not in self.vertices or w not in self.vertices:
			return False
			
		else:
			self.aristas[clave] = peso
			w.agregar_adyacente(v, peso)
			v.agregar_adyacente(w, peso)
			return True
	
	def estan_conectados(self, v, w):
		if v not in self.vertices or w not in self.vertices:
			return False
			
		else:
			if v.obtener_adyacente()[w.clave]:
				return True
				
			else:
				return False
		
	def obtener_vertice(self, v):
		for w in self.vertices:
			if w.obtener_clave() == v:
				return w.obtener_valor()
				
		return None
		
	def obtener_adyacentes(self, v):
		if v not in self.vertices:
			return None
			
		else:
			return v.obtener_adyacente()
	
	def obtener_arista(self, v, w):
		lista1 = [v, w]
		clave1 = ",".join(lista1)
		lista2 = [w, v]
		clave2 = ",".join(lista2)

		for clave in self.aristas.keys():
			if clave == clave1 or clave == clave2:
				return self.aristas[clave]

		else:
			return None


	def obtener_largo(self):
		return len(self.vertices)
		
	def __iter__(self):
		return iter(self.vertices.values())