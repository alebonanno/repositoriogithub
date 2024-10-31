from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    # Atributos de clase
    _id = None
    _nombre = None

    # Constructor
    @abstractmethod    
    def __init__(self, id, nombre: str) -> None:
        self._id = id
        self._nombre = nombre
    #Comandos
    def establecerNombre(self, nombre: str) -> None:
        self._nombre = nombre

    #Consultas
    def obtenerId(self) -> str:
        return self._id

    def obtenerNombre(self) -> str:
        return self._nombre
    
    # Sobrescritura del método __eq__ para comparar por id
    def __eq__(self, otro) -> bool:
        if isinstance(otro, EntidadVineria):
            return self._id == otro.obtenerId()
        return False