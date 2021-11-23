from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado) 

    @staticmethod
    def movimiento():
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        a = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return a

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        a = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return a

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getColorEscamas(self):
        return self._colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso