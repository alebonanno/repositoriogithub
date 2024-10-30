from abc import ABC


class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        super().__init__()
        self.__id = id
        self.__nombre = nombre

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def __eq__(self, entidadVineria):
        return (
            isinstance(entidadVineria, EntidadVineria)
            and self.obtenerId() == entidadVineria.obtenerId()
        )
