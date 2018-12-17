#!/usr/bin/python3

class Arista(object):
	def __init__(self, aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos):
		self.conexion = {aeropuerto1, aeropuerto2}
		self.tiempo = tiempo
		self.precio = precio
		self.cant_vuelos = cant_vuelos

	def obtener_conexion_aeropuertos(self):
		return self.conexion

	def obtener_tiempo(self):
		return self.tiempo

	def obtener_cant_vuelos(self):
		return self.cant_vuelos

	def obtener_precio(self):
		return self.precio


class Vertice(object):
	def __init__(self, ciudad, codigo):
		self.ciudad = ciudad
		self.codigo = codigo
		self.adyacentes = {}

	def obtener_adyacentes(self):
		return self.adyacentes

	def agregar_adyacente(self, adyacente):
		self.adyacentes.lista.append(adyacente)

	def obtener_codigo(self):
		return self.codigo
		
	def obtener_ciudad(self):
		return self.ciudad
		

class Grafo(object):
	def __init__(self):
		self.vertices = {}
		self.aristas = {}
		self.codigos = {}

	def agregar_vertice(self, ciudad, codigo):
		if codigo not in self.codigos()
			v = Vertice(ciudad, codigo)
			self.vertices[codigo] = v
			self.codigos.lista.append(codigo)

	
	def agregar_arista(self, aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos):
		e = Arista(aeropuerto1, aeropuerto2, tiempo, precio, cant_vuelos)
		Vertice.agregar_adyacente(aeropuerto1, aeropuerto2)
		Vertice.agregar_adyacente(aeropuerto2,aeropuerto1)
		self.aristas.lista.append(e)

	def estan_conectados(self, codigo1, codigo2):
		if codigo1 in self.vertices.codigos() and codigo2 in self.vertices.codigos():
			return True
		return False


	def obtener_vertice(self, codigo):
		if len(self.vertices) == 0:
			return None
		
		for i in range(0, len(self.vertices)):
			if(self.codigos[i] == codigo)
				return  self.vertices[i]


	def obtener_adyacentes(self, codigo):
		if codigo in self.codigos():
			return Vertice.obtener_adyacentes(self.vertices[codigo])


	def obtener_largo(self):
		return len(self.vertices)
		
	def __iter__(self):
		return iter(self.vertices.values())
