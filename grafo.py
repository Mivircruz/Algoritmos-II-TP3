
class Vertice(object):
	def __init__(self, ciudad, codigo, latitud, longitud):
		self.vertice = {codigo: (ciudad, latitud, longitud)}
		self.adyacentes = {}

	def obtener_codigo(self):
		return self.vertice[codigo]
		
	def obtener_ciudad(self):
		return self.vertice.keys()

	def agregar_adyacente(self, codigo, codigo_ady, tiempo, precio, cant_vuelos):
		self.adyacentes[codigo] = {codigo_ady : (tiempo, precio, cant_vuelos)}

	def son_adyacentes(self, codigo_ady):
		if codigo_ady in self.adyacentes:
			return  True
		return False
	def obtener_adyacentes(self):
		return self.adyacentes
		

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
		if codigo not in self.vertices:
			self.vertices[codigo] = Vertice(ciudad,codigo,latitud,longitud)

	
	def agregar_arista(self, aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos):
		self.vertices.get(aeropuerto1).agregar_adyacente(self.vertices[aeropuerto1],aeropuerto1,  aeropuerto2, tiempo, precio, cant_vuelos)
		self.vertices.get(aeropuerto2).agregar_adyacente(self.vertices[aeropuerto2],aeropuerto2,  aeropuerto1, tiempo, precio, cant_vuelos)

	def estan_conectados(self, codigo1, codigo2):
		return self.vertices.get(codigo1).son_adyacentes(self.vertices[codigo1],codigo2)


	def obtener_vertice(self, codigo):
		if len(self.vertices) == 0:
			return None
		return self.vertices.get(codigo)


	def obtener_adyacentes(self, codigo):

		return self.vertices.get(codigo).obtener_adyacentes(self.vertices[codigo])


	def obtener_largo(self):
		return len(self.vertices)


	#NO SÉ QUÉ ODNA ESTE MÉTODO:

	def __iter__(self):
		return iter(self.vertices.values)
