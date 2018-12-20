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

    def agregar_adyacente(self, ciudad, tiempo, precio, cant_vuelos):
        self.adyacentes[ciudad] = [tiempo, precio, cant_vuelos]

    def obtener_adyacente(self, ciudad):
        return self.adyacentes[ciudad]

    def son_adyacentes(self, ciudad_ady):
        if ciudad_ady in self.adyacentes:
            return True
        return False

    def obtener_adyacentes(self):
        return self.adyacentes
