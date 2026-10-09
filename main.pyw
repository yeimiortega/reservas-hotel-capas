"""Abre la aplicación con ventana gráfica (doble clic, sin terminal)."""
from datos.repositorio_json import RepositorioJSON
from negocio.servicio_hotel import ServicioHotel
from presentacion.ventana import VentanaHotel

if __name__ == "__main__":
    VentanaHotel(ServicioHotel(RepositorioJSON("datos_hotel.json"))).ejecutar()
