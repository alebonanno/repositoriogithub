# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    def obtenerBodegas(orden=None, reverso=False):
        bodegas = Vinoteca.__bodegas.copy()
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas.sort(key=lambda b: b.obtenerNombre(), reserse=reverso)
            elif orden == "vinos":
                bodegas.sort(key=lambda b: len(b.obtenerVinos()), reserse=reverso)
        return bodegas

    def obtenerCepas(orden=None, reverso=False):
        cepas = Vinoteca.__cepas.copy()
        if isinstance(orden, str):
            if orden == "nombre":
                cepas.sort(key=lambda c: c.obtenerNombre(), reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False):
        vinos = Vinoteca.__vinos.copy()
        if isinstance(anio, int):
            vinos = [vino for vino in vinos if anio in vino.obtenerPartidas()]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos.sort(key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos.sort(
                    key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso
                )
            elif orden == "cepas":
                vinos.sort(key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        return vinos

    def buscarBodega(id):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    def __parsearArchivoDeDatos():
        with open(Vinoteca.__archivoDeDatos, "r") as archivo:
            datos = json.load(archivo)
        return datos

    def __convertirJsonAListas(lista):
        for bodega_data in lista["bodegas"]:
            bodega = Bodega(bodega_data["id"], bodega_data["nombre"])
            Vinoteca.__bodegas.append(bodega)

        for cepa_data in lista["cepas"]:
            cepa = Cepa(cepa_data["id"], cepa_data["nombre"])
            Vinoteca.__cepas.append(cepa)

        for vino_data in lista["vinos"]:
            vino = Vino(
                vino_data["id"],
                vino_data["nombre"],
                vino_data["bodega"],
                vino_data["cepas"],
                vino_data["partidas"],
            )
            Vinoteca.__vinos.append(vino)
