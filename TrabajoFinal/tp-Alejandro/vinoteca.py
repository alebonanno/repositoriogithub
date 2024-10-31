# librerias
import os
import json

# modelos
# from modelos.bodega import Bodega
# from modelos.cepa import Cepa
# from modelos.vino import Vino

class Vinoteca:
    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @staticmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    @staticmethod
    def __parsearArchivoDeDatos() -> dict:
        try:
            with open(Vinoteca.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
                datos_json = json.load(archivo)
            return datos_json
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {Vinoteca.__archivoDeDatos}.")
            return {}
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            return {}

    @staticmethod
    def __convertirJsonAListas(datos: dict) -> None:
        from bodega import Bodega
        from cepa import Cepa
        from vino import Vino
    
        lista = datos.get("bodegas", [])
        for item in lista:
            inst = Bodega(item["id"],item["nombre"])
            Vinoteca.__bodegas.append(inst)
            
        lista = datos.get("cepas", [])
        for item in lista:
            inst = Cepa(item["id"], item["nombre"])
            Vinoteca.__cepas.append(inst)
        lista = datos.get("vinos", [])
        for item in lista:
            inst = Vino(item["id"], item["nombre"], item["bodega"], item["cepas"], item["partidas"])
            Vinoteca.__vinos.append(inst)
            
       
    def obtenerBodegas(orden = None, reverso=False) -> list['Bodega']: #type: ignore
        #from bodega import Bodega
        try:
            if isinstance(orden, str):
                lista = Vinoteca.__bodegas
                if orden == "id":
                    print(f"Lista de bodegas ordenadas según el campo {orden} en orden {'inverso' if reverso else 'directo'}")
                    return sorted(lista, key=lambda b: b.obtenerId(), reverse=reverso)
                elif orden == "nombre":
                    print(f"Lista de bodegas ordenadas según el campo {orden} en orden {'inverso' if reverso else 'directo'}")
                    return sorted(lista, key=lambda b: b.obtenerNombre(), reverse=reverso)
                else:
                    raise ValueError("El parámetro 'orden' no es válido. Use 'id' o 'nombre'.")

            else:
                print("Lista sin ordenar.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

        return Vinoteca.__bodegas

    def obtenerCepas(orden=None, reverso=False) -> list['Vino']: #type: ignore
        try:
            lista = Vinoteca.__cepas
            if isinstance(orden, str):
                
                print(f"Lista de cepas ordenadas según el campo {orden} en orden {'inverso' if reverso else 'directo'}")
                if orden == "id":
                    print(f"Lista de cepas ordenadas según el campo {orden} en orden {'inverso' if reverso else 'directo'}")
                    return sorted(lista, key=lambda b: b.obtenerId(), reverse=reverso)
                elif orden == "nombre":
                    print(f"Lista de cepas ordenadas según el campo {orden} en orden {'inverso' if reverso else 'directo'}")
                    return sorted(lista, key=lambda b: b.obtenerNombre(), reverse=reverso)
                else:
                    raise ValueError("El parámetro 'orden' no es válido. Use 'id' o 'nombre'.")
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
        return Vinoteca.__cepas
    
    
    def obtenerVinos(anio=None, orden=None, reverso=False) -> list['Vino']: #type: ignore
        from vino import Vino
        try:
            listVinosAnio = []
            if isinstance(anio, int):
                for vino in Vinoteca.__vinos:
                    if anio in vino.obtenerPartidas():
                        listVinosAnio.append(vino)
                if len(listVinosAnio)==0:
                    print(f"No se encontraron vinos del año: {anio}")
                
            else:
                listVinosAnio = Vinoteca.__vinos
                
            # Eliminar duplicados, si es necesario
            vinos = []
            for vino in listVinosAnio:
                if vino not in vinos:
                    vinos.append(vino)          
                    
            if orden is None:
                if reverso:
                    return vinos[::-1]
                else:
                    return vinos  
            
            if isinstance(orden, str):
                if orden == "id":
                    #print(f"Lista de vinos ordenados según el campo id en orden {'inverso' if reverso else 'directo'}")
                    return sorted(vinos, key=lambda b: b.obtenerId(), reverse=reverso)
                if orden == "nombre":
                    #print(f"Lista de vinos ordenados según el campo nombre en orden {'inverso' if reverso else 'directo'}")
                    return sorted(vinos, key=lambda b: b.obtenerNombre(), reverse=reverso)
                elif orden == "bodega":
                    #print(f"Lista de vinos ordenados según el campo nombre de bodega en orden {'inverso' if reverso else 'directo'}")
                    # print(vinos[0])
                    # print(isinstance(vinos[0], Vino))
                    # print(f" bodega: {vinos[0].obtenerBodega()}")
                    return sorted(vinos, key=lambda b: b.obtenerBodega().obtenerNombre(), reverse=reverso)
                elif orden == "cepas":
                    #print(f"Lista de vinos ordenados según el campo cantidad de cepas en orden {'inverso' if reverso else 'directo'}")
                    return sorted(vinos, key=lambda b: len(b['cepas']), reverse=reverso)
                elif orden == "partidas":
                    #print(f"Lista de vinos ordenados según el campo cantidad de partidas en orden {'inverso' if reverso else 'directo'}")
                    return sorted(vinos, key=lambda b: len(b['partidas']), reverse=reverso)
                else:
                    raise ValueError("El parámetro 'orden' no es válido, debe ser nombre, bodega, cepas o partidas.")
            else:
                raise TypeError("El parámetro 'orden' debe ser una cadena de texto válida.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

        return vinos
    
    
    def buscarBodega(id: str) -> 'Bodega': # type: ignore
        from bodega import Bodega
        id = str(id)
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
    
    
    def buscarCepa(id: str) -> 'Cepa':
        from cepa import Cepa
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
    
    def buscarVino(id: str) -> 'Vino': #type: ignore
        from vino import Vino
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    

if __name__ == '__main__': 
    from cepa import Cepa
    Vinoteca.inicializar()
    #print(Vinoteca.obtenerBodegas())  # Devuelve la lista original sin ordenar
    #URL: http://127.0.0.1:5000/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8
    #print(Vinoteca.buscarBodega("a0900e61-0f72-67ae-7e9d-4218da29b7d8"))
    #URL: http://127.0.0.1:5000/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d 
    #URL: http://127.0.0.1:5000/api/vinos/4823ad54-0a3a-38b8-adf6-795512994a4f
    #URL: http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=no
    #URL: http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=si
    #print(Vinoteca.obtenerVinos(2023,None,False))
    #print(Vinoteca.obtenerCepas())
    #print(Vinoteca.vino())
    #print(isinstance(Vinoteca.vino(), list))
    #print(isinstance(Vinoteca._Vinoteca__bodegas[0], Bodega))
    #print(Vinoteca._Vinoteca__bodegas)
    #print(Vinoteca.obtenerBodegas())
    #print(Vinoteca.obtenerBodegas("nombro", True))
    #print(Vinoteca.obtenerBodegas("nombre",True))
    #print(Vinoteca.obtenerCepas())
    #print(Vinoteca.buscarCepa("33ccaa9d-4710-9942-002d-1b5cb9912e5d"))
    # print(Vinoteca.obtenerCepas(True))
    print(f"buscar bodega {Vinoteca.buscarBodega("a0900e61-0f72-67ae-7e9d-4218da29b7d8")}")
    print(type(Vinoteca.buscarBodega("a0900e61-0f72-67ae-7e9d-4218da29b7d8")))
    #print(Vinoteca.obtenerVinos(2020,"bodega"))
    # print(Vinoteca.obtenerVinos())
    # print(Vinoteca.buscarBodega("cd32d0ab-1da5-7d5e-caff-f90bbee6fe7f"))
    # print(isinstance(Vinoteca.buscarCepa("e076a2c8-b1f5-136e-8319-0ee0b5c02091"), Cepa))
    # print(f"Buscando bodega del vino La Iride: {Vinoteca.buscarBodega("a0117be3-2ea6-8db1-8901-1be2adf61c29")}")
    # print(Vinoteca.buscarVino("54919dcb-7ada-70ee-db7d-605650ee41f7"))