"""Punto de entrada: ensambla las tres capas (datos -> negocio -> presentación)."""
from datos.repositorio_json import RepositorioJSON
from negocio.servicio_hotel import ServicioHotel
from presentacion.consola import ConsolaHotel

if __name__ == "__main__":
    ConsolaHotel(ServicioHotel(RepositorioJSON("datos_hotel.json"))).ejecutar()
