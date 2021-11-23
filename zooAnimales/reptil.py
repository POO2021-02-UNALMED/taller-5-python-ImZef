from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, largoCola, colorEscamas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._largoCola = largoCola
        self._colorEscamas = colorEscamas
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)    

    @staticmethod
    def movimiento():
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        a = Reptil(nombre, edad, "humedal", genero, 3, "verde")
        return a

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.iguanas += 1
        a = Reptil(nombre, edad, "jungla", genero, 1, "blanco")
        return 
        
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    def getLargoCola(self):
        return self._largoCola

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas