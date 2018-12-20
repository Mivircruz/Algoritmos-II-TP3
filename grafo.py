
import vertice

'''''
casimiropastine@gmail.com


vertices = {
	
	cod1: {ciudad: (lat, long)}
	
	cod2: {ciudad: (lat, long)}
	
	cod3: {}

}


aristas = {
	cod1: {cod5: (tiempo, precio, cant), cod2: (tiempo, precio, cant)}
	cod2: {cod1: (tiempo, precio, cant)}
	cod3: {cod4: (tiempo, precio, cant), cod8: (tiempo, precio, cant)}
	cod 5: {cod1: (tiempo, precio, cant)}
}

'''''

#Grafo implementado como diccionario de diccionarios

class Grafo(object):

	def __init__(self):
		self.vertices = {}

	def agregar_vertice(self, ciudad, codigo, latitud, longitud):

		self.vertices[ciudad] = vertice.Vertice(ciudad, codigo, latitud, longitud)

	
	def agregar_arista(self, ciudad1, ciudad2, tiempo, precio, cant_vuelos):

		self.vertices[ciudad1].agregar_adyacente(ciudad2, tiempo, precio, cant_vuelos)
		self.vertices[ciudad2].agregar_adyacente(ciudad1, tiempo, precio, cant_vuelos)

	def estan_conectados(self, ciudad1, ciudad2):
		return vertice.son_adyacentes(self.vertices[ciudad1], ciudad2)


	def obtener_vertice(self, ciudad):
		return self.vertices.get(ciudad)

	def obtener_todos_vertices(self):
		return self.vertices


	def obtener_adyacentes(self, ciudad):
		return self.vertices[ciudad].obtener_adyacentes()

	def obtener_tiempo(self, ciudad1, ciudad2):
		if ciudad1 in self.vertices.keys():
			if ciudad2 in self.vertices[ciudad1].adyacentes.keys():
				datos_conexion = self.vertices[ciudad1].adyacentes[ciudad2]
				return datos_conexion[0]

		return None

	def obtener_precio(self, ciudad1, ciudad2):
		if ciudad1 in self.vertices.keys():
			if ciudad2 in self.vertices[ciudad1].adyacentes.keys():
				datos_conexion = self.vertices[ciudad1].adyacentes[ciudad2]
				return datos_conexion[1]

		return None

	def obtener_cant_vuelos(self, ciudad1, ciudad2):
		if ciudad1 in self.vertices.keys():
			if ciudad2 in self.vertices[ciudad1].adyacentes.keys():
				datos_conexion = self.vertices[ciudad1].adyacentes[ciudad2]
				return datos_conexion[2]

		return None

	def obtener_largo(self):
		return len(self.vertices)

	def pertenece(self, ciudad):
		if ciudad not in self.vertices:
			return False
		return True

	def __iter__(self):
		return iter(self.vertices.values)
