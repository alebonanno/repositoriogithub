import json
from modelos.entidadvineria import EntidadVineria


class Vino(EntidadVineria):

    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

    def obtenerPartidas(self):
        return self.__partidas

    def obtenerBodega(self):
        from vinoteca import Vinoteca

        return Vinoteca.buscarBodega(self.__bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca

        cepasDelVino = []
        for cepaId in self.__cepas:
            cepasDelVino.append(Vinoteca.buscarCepa(cepaId))
        return cepasDelVino

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
