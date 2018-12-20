class Vertice(object):

    def __init__(self, ciudad, codigo, latitud, longitud):
        self.codigo = codigo
        self.ciudad = ciudad
        self.latitud = latitud
        self.longitud = longitud
        self.adyacentes = {}

    def obtener_codigo(self):
        return self.codigo

    def obtener_ciudad(self):
        return self.ciudad

    def agregar_adyacente(self, codigo, tiempo, precio, cant_vuelos):
        self.adyacentes[codigo] = [tiempo, precio, cant_vuelos]

    def obtener_adyacente(self, codigo):
        return self.adyacentes[codigo]

    def son_adyacentes(self, codigo_ady):
        if codigo_ady in self.adyacentes:
            return True
        return False

    def obtener_adyacentes(self):
        return self.adyacentes

    def obtener_tiempo(self, codigo):
        datos_conexion = self.adyacentes.get(codigo)
        return datos_conexion[0]

    def obtener_precio(self, codigo):
        datos_conexion = self.adyacentes.get(codigo)
        return datos_conexion[1]

    def obtener_cant_vuelos(self, codigo):
        datos_conexion = self.adyacentes.get(codigo)
        return datos_conexion[2]
