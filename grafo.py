
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

		self.vertices[codigo] = vertice.Vertice(ciudad,codigo,latitud,longitud)

	
	def agregar_arista(self, aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos):

		vertice.agregar_adyacente(self.vertices[aeropuerto1],aeropuerto1,  aeropuerto2, tiempo, precio, cant_vuelos)
		vertice.agregar_adyacente(self.vertices[aeropuerto2],aeropuerto2,  aeropuerto1, tiempo, precio, cant_vuelos)

	def estan_conectados(self, codigo1, codigo2):
		return vertice.son_adyacentes(self.vertices[codigo1],codigo2)


	def obtener_vertice(self, codigo):
		return self.vertices.get(codigo)

	def obtener_todos_vertices(self):
		return self.vertices


	def obtener_adyacentes(self, codigo):
		return vertice.obtener_adyacentes(self.vertices[codigo])


	def obtener_largo(self):
		return len(self.vertices)

	def pertenece(self, codigo):
		if codigo not in self.vertices:
			return False
		return True

	def __iter__(self):
		return iter(self.vertices.values)
