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
		self.vertices = {}

	def agregar_vertice(self, clave, valor):
		v = Vertice(clave, valor)
		if v not in self.vertices:
			self.vertices[clave] = v
			return True
		
		else:
			return False
	
	def agregar_arista(self, clave1, clave2, peso=0):
		if clave1 in self.vertices.keys():
			v = self.vertices[clave1]
			if clave2 in self.vertices.keys():
				w = self.vertices[clave2]
				v.agregar_adyacente(w, peso)
				w.agregar_adyacente(v, peso)
				return True

		return False

	
	def estan_conectados(self, clave1, clave2):
		if clave1 in self.vertices.keys():
			v = self.vertices[clave1]
			adyacentes = v.obtener_adyacente()
			if clave2 in adyacentes.keys():
				return True

		return False


	def obtener_vertice(self):
		if len(self.vertices) == 0:
			return None
		
		for i in self.vertices.keys():
			v = self.vertices[i]

		diccionario = {}
		diccionario[v.obtener_clave()] = v.obtener_valor()
		return diccionario	

	def obtener_adyacentes(self, clave):
		if clave in self.vertices.keys():
			v = self.vertices[clave]
			return v.obtener_adyacente()

		return None
	
	def obtener_arista(self, clave1, clave2):
		if clave1 in self.vertices.keys():
			v = self.vertices[clave1]
			adyacentes = v.obtener_adyacente()
			if clave2 in adyacentes.keys():
				return adyacentes[clave1]
		
		return None


	def obtener_largo(self):
		return len(self.vertices)
		
	def __iter__(self):
		return iter(self.vertices.values())
