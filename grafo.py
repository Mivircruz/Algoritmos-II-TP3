
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
		self.codigos = {}

	def agregar_vertice(self, ciudad, codigo, latitud, longitud):

		self.vertices[codigo] = vertice.Vertice(ciudad, codigo, latitud, longitud)
		self.codigos[ciudad] = codigo

	def obtener_codigo(self, ciudad):
		return self.codigos.get(ciudad)

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


	def obtener_adyacentes(self, codigo):
		return self.vertices[codigo].obtener_adyacentes()

	def obtener_tiempo(self, codigo1, codigo2):
		if codigo1 in self.vertices.keys():
			if codigo2 in self.vertices[codigo1].adyacentes.keys():
				datos_conexion = self.vertices[codigo1].adyacentes[codigo2]
				return datos_conexion[0]

		return None

	def obtener_precio(self, codigo1, codigo2):
		if codigo1 in self.vertices.keys():
			if codigo2 in self.vertices[codigo1].adyacentes.keys():
				datos_conexion = self.vertices[codigo1].adyacentes[codigo2]
				return datos_conexion[1]

		return None

	def obtener_cant_vuelos(self, codigo1, codigo2):
		if codigo1 in self.vertices.keys():
			if codigo2 in self.vertices[codigo1].adyacentes.keys():
				datos_conexion = self.vertices[codigo1].adyacentes[codigo2]
				return datos_conexion[2]

		return None

	def obtener_largo(self):
		return len(self.vertices)

	def pertenece(self, codigo):
		if codigo not in self.vertices:
			return False
		return True

	def __iter__(self):
		return iter(self.vertices.values)
