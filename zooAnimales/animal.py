



class Animal:

    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    @staticmethod
    def movimiento():
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\nAves: " + str(Ave.cantidadAves()) + "\nReptiles: " + str(Reptil.cantidadReptiles()) + "\nPeces: " + str(Pez.cantidadPeces()) + "\nAnfibios: " + str(Anfibio.cantidadAnfibios()) 

    def toSting(self):
        
        from gestion.zona import Zona
        from gestion.zoologico import Zoologico

        if(type(self._zona) != None):
            return "Mi nombre es " + self._nombre + ", tengo una edad de "+  str(self._edad) + ",habito en " + self._habitat + " y mi genero es " + self._genero + ",la zona en la que me ubico es " + self._zona.getNombre() + ", en el"  + self._zona.getZoo().getNombre()
        
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de "+  str(self._edad) + ",habito en " + self._habitat + " y mi genero es " + self._genero

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getHabitat(self):
        return self._habitat

    def setGenero(self, genero):
        self._genero = genero

    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona

    def getNombre(self):
        return self._zona