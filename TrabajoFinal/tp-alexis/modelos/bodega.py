import json

from modelos.entidadvineria import EntidadVineria


class Bodega(EntidadVineria):

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

    def obtenerVinos(self):
        from vinoteca import Vinoteca

        vinos = Vinoteca.obtenerVinos()
        vinosBodega = list(
            filter(lambda v: (v.obtenerBodega().obtenerId() == self.obtenerId()), vinos)
        )
        return vinosBodega

    def obtenerCepas(self):
        from vinoteca import Vinoteca

        vinosBodega = self.obtenerVinos()
        cepasIds = []
        for vino in vinosBodega:
            vinoCepas = vino.obtenerCepas()
            for vinoCepa in vinoCepas:
                vinoCepaId = vinoCepa.obtenerId()
                if vinoCepaId not in cepasIds:
                    cepasIds.append(vinoCepaId)

        cepas = []
        for cepaId in cepasIds:
            cepas.append(Vinoteca.buscarCepa(cepaId))

        return cepas
