import json

from entidadvineria import EntidadVineria


class Cepa(EntidadVineria):
    #Atributos de clase
    #Atributos de instancia
    
    #Constructores
    def __init__(self, id, nombre: str) -> None:
        super().__init__(id, nombre)
        
    #Comandos
    
    #Consultas
    def obtenerVinos(self) -> list['Vino']: #type: ignore
        from vinoteca import Vinoteca
        vinosDeCepa = []
        # Recorrer la lista de vinos y filtrar según el id de la bodega
        for vino in Vinoteca.obtenerVinos("bodega"):
            for cepa in  vino.obtenerCepas():
                if cepa.obtenerId() == self.obtenerId():
                    vinosDeCepa.append(vino)
        # Eliminar duplicados, si es necesario
        vinos = []
        for vino in vinosDeCepa:
            if vino not in vinos:
                vinos.append(vino)
        return vinos     


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

    def __mapearVinos(self) -> list[str]: 
        from vino import Vino
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)


if __name__ == '__main__': 
    from vinoteca import Vinoteca
    Vinoteca.inicializar()
    print(f"Cepa: {Vinoteca.buscarCepa("33ccaa9d-4710-9942-002d-1b5cb9912e5d")}")
    print(f"Produce estos vinos: {Vinoteca.buscarCepa("33ccaa9d-4710-9942-002d-1b5cb9912e5d").obtenerVinos()}")
    print(f"Cepa: {Vinoteca.buscarCepa("b065c64b-fc96-cf13-2d52-d7a6ba373c68")}")
    print(f"Produce estos vinos: {Vinoteca.buscarCepa("b065c64b-fc96-cf13-2d52-d7a6ba373c68").obtenerVinos()}")
    print(f"Cepa: {Vinoteca.buscarCepa("e076a2c8-b1f5-136e-8319-0ee0b5c02091")}")
    print(f"Produce estos vinos: {Vinoteca.buscarCepa("e076a2c8-b1f5-136e-8319-0ee0b5c02091").obtenerVinos()}")
    print(f"Cepa: {Vinoteca.buscarCepa("b80905e3-1839-3194-301b-c5fddafc888c")}")
    print(f"Produce estos vinos: {Vinoteca.buscarCepa("b80905e3-1839-3194-301b-c5fddafc888c").obtenerVinos()}")