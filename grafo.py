#!/usr/bin/python3



class Vertice(object):
	def __init__(self, ciudad, codigo, latitud, longitud):
		self.vertice = {codigo: (ciudad, latitud, longitud)}

	def obtener_codigo(self):
		return self.vertice[codigo]
		
	def obtener_ciudad(self):
		return self.vertice.keys()
		

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

class Grafo(object):
	def __init__(self):
		self.vertices = []
		self.aristas = {}

	def agregar_vertice(self, ciudad, codigo, latitud, longitud):
		if codigo not in self.vertices:
			self.vertices.append(Vertice(ciudad, codigo, latidud, longitud))

	
	def agregar_arista(self, aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos):
		if aeropuerto1 not in self.aristas:
			self.aristas[aeropuerto1] = {}

		self.aristas[aeropuerto1][aeropuerto2] = (tiempo, precio, cant_vuelos)

		if aeropuerto2 not in self.aristas:
			self.aristas[aeropuerto2] = {}

		self.aristas[aeropuerto2][aeropuerto1] = (tiempo, precio, cant_vuelos)
		

	def estan_conectados(self, codigo1, codigo2):
		if codigo1 in self.vertices.codigos() and codigo2 in self.vertices.codigos():
			return True
		return False


	def obtener_vertice(self, codigo):
		if len(self.vertices) == 0:
			return None
		
		for i in range(0, len(self.vertices)):
			if self.codigos[i] == codigo:
				return  self.vertices[i]


	def obtener_adyacentes(self, codigo):
		if codigo in self.codigos:
			return Vertice.obtener_adyacentes(self.vertices[codigo])


	def obtener_largo(self):
		return len(self.vertices)
		
	def __iter__(self):
		return iter(self.vertices.values)
