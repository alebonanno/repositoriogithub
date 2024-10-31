import json

from entidadvineria import EntidadVineria
from cepa import Cepa
from bodega import Bodega

class Vino(EntidadVineria):
    #Atributos de clase
    #Atributos de instancia
    
    #Constructores
    def __init__(self, id: int, nombre: str, bodega: str, cepas: list[str], partidas: list[int]):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas
        
         
    #Comandos
    def establecerNombre(self, nombre: str) -> None:
        return super().establecerNombre(nombre)
    
    def establecerBodega(self, bodega: str) -> None:
        self.__bodega = bodega
        
    def establecerCepas(self, cepas: list[str]) -> None:
        self.__cepas = cepas
        
    def establecerPartidas(self, partidas: list[int]) -> None:
        self.__partidas = partidas
        
    #Consultas
    def obtenerId(self) -> str:
        return super().obtenerId()
    
    def obtenerNombre(self) -> str:
        return super().obtenerNombre()
    

    def obtenerBodega(self) -> Bodega:
        from vinoteca import Vinoteca
        bodega = Vinoteca.buscarBodega(self.__bodega)
        return bodega
    
    def obtenerCepas(self) -> list[Cepa]:
        from vinoteca import Vinoteca
        listaCepas = []
        for cepa in self.__cepas:
            c = Vinoteca.buscarCepa(cepa)
            listaCepas.append(c)
        return listaCepas
    
    def obtenerPartidas(self) -> list[int]:
        return self.__partidas
    
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

    def __mapearCepas(self) -> list[str]:
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

if __name__ == '__main__': 
    from vinoteca import Vinoteca
    Vinoteca.inicializar()
    print(f"Buscando vino {Vinoteca.buscarVino("54919dcb-7ada-70ee-db7d-605650ee41f7")}")
    print(f"De Bodega {Vinoteca.buscarVino("54919dcb-7ada-70ee-db7d-605650ee41f7").obtenerBodega()}")  
    print(f"De Cepas {Vinoteca.buscarVino("54919dcb-7ada-70ee-db7d-605650ee41f7").obtenerCepas()}")    
    # print(f"Buscando bodega del vino La Iride: {Vinoteca.buscarBodega("a0117be3-2ea6-8db1-8901-1be2adf61c29")}")