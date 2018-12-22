
import vertice

#Grafo implementado como diccionario de diccionarios

class Grafo(object):

	def __init__(self):
		self.vertices = {}

	def agregar_vertice(self, ciudad, codigo, latitud, longitud):

		self.vertices[codigo] = vertice.Vertice(ciudad, codigo, latitud, longitud)

	def obtener_ciudad(self, codigo):
		return self.vertices[codigo].obtener_ciudad()

	def agregar_arista(self, codigo1, codigo2, tiempo, precio, cant_vuelos):

		self.vertices[codigo1].agregar_adyacente(codigo2, tiempo, precio, cant_vuelos)
		self.vertices[codigo2].agregar_adyacente(codigo1, tiempo, precio, cant_vuelos)


	def estan_conectados(self, codigo1, codigo2):
		return vertice.son_adyacentes(self.vertices[codigo1], codigo2)


	def obtener_vertice(self, codigo):
		return self.vertices.get(codigo)

	def obtener_todos_vertices(self):
		return self.vertices

	def obtener_aeropuertos(self, ciudad):

		lista_aeropuertos = []

		for key,value in self.vertices:
			if value.obtener_ciudad() == ciudad:
				lista_aeropuertos.append(value)
		return lista_aeropuertos

	def obtener_adyacentes(self, codigo):
		return self.vertices[codigo].obtener_adyacentes()

	def obtener_tiempo(self, codigo1, codigo2):
		return self.vertices[codigo1].obtener_tiempo(codigo2)

	def obtener_precio(self, codigo1, codigo2):
		return self.vertices[codigo1].obtener_precio(codigo2)

	def obtener_cant_vuelos(self, codigo1, codigo2):
		return self.vertices[codigo1].obtener_cant_vuelos(codigo2)

	def obtener_largo(self):
		return len(self.vertices)

	def pertenece(self, codigo):
		if codigo not in self.vertices:
			return False
		return True

	def __iter__(self):
		return iter(self.vertices.values)
