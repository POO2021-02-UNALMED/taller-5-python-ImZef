from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        a = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return a

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.leones += 1
        a = Mamifero(nombre, edad, "selva", genero, True, 4)
        return a

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def isPelaje(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas