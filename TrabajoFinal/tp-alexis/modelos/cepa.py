import json

from modelos.entidadvineria import EntidadVineria


class Cepa(EntidadVineria):

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)

    def obtenerVinos(self):
        from vinoteca import Vinoteca

        vinos = Vinoteca.obtenerVinos()
        vinosCepa = []
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                if cepa.obtenerId() == self.obtenerId():
                    vinosCepa.append(vino)
                    break
        return vinosCepa
