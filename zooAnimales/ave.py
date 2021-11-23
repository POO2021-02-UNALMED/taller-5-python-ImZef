from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @staticmethod
    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        a = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return a
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        a = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        return a

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    def getColorPlumas(self):
        return self._colorPlumas