from entidadvineria import EntidadVineria
import json

class Bodega(EntidadVineria):
    #Atributos de clase
    #Atributos de instancias
    
    #Constructores
    def __init__(self, id, nombre: str) -> None:
        super().__init__(id, nombre)
        
    #Comandos
    #Consultas
    def obtenerVinos(self) -> list['Vino']: #type: ignore
        from vinoteca import Vinoteca
        vinosFiltrados = []
        # Recorrer la lista de vinos y filtrar según el id de la bodega
        for vino in Vinoteca.obtenerVinos(None,"bodega"):
            if vino.obtenerBodega().obtenerId() == self.obtenerId():
                vinosFiltrados.append(vino)
        # Eliminar duplicados, si es necesario
        vinos = []
        for vino in vinosFiltrados:
            if vino not in vinos:
                vinos.append(vino)
        return vinos
    
    def obtenerCepas(self) -> list['Cepa']: #type: ignore
        from vinoteca import Vinoteca
        cepasFiltradas = []
        # Recorrer la lista de vinos y filtrar según el id de la bodega
        for vino in Vinoteca.obtenerVinos("bodega"):
            if vino.obtenerBodega().obtenerId() == self.obtenerId():
                cepasFiltradas.extend(vino.obtenerCepas())  # Agregar las cepas a la lista
        # Eliminar duplicados, si es necesario
        cepas = []
        for cepa in cepasFiltradas:
            if cepa not in cepas:
                cepas.append(cepa)
        return cepas
    
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

    def __mapearCepas(self) -> list[str]:
        from cepa import Cepa
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self) -> list[str]:
        from vino import Vino
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

if __name__ == '__main__': 
    from vinoteca import Vinoteca
    Vinoteca.inicializar()    
    print(Vinoteca.buscarBodega("a0900e61-0f72-67ae-7e9d-4218da29b7d8"))
    #print(bodega.obtenerVinos())
    #print(bodega.obtenerCepas())
    