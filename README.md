# Reservas de habitaciones de un hotel (Caso 06)

Aplicación de consola en Python con **arquitectura por capas**: presentación, negocio y acceso a datos.

## Requisitos
- Python 3.10 o superior (probado con 3.13). Sin librerías externas.

## Ejecutar
**Con ventana (recomendado):** doble clic en `main.pyw`. En Windows también funciona `python main.pyw` o el botón ▶ de VS Code con `main.pyw` abierto.

**Con consola:**
```
cd hotel
python main.py
```
(Tkinter viene incluido con Python en Windows.)
Los datos se guardan en `datos_hotel.json` (se crea solo) y se conservan al cerrar y volver a abrir.
Fechas con formato `AAAA-MM-DD`.

## Pruebas
```
python -m unittest -v
```
Las pruebas 1 a 5 (`test1_...` a `test5_...`) son las cinco mínimas del caso; el resto son pruebas adicionales de errores y límites.

## Estructura
| Carpeta / archivo | Capa | Responsabilidad |
|---|---|---|
| `presentacion/ventana.py` | Presentación | Ventana Tkinter con pestañas. Sin reglas. |
| `presentacion/consola.py` | Presentación | Alternativa en consola (menú de texto). Sin reglas. |
| `negocio/servicio_hotel.py` | Negocio | Todas las reglas del caso y las operaciones. |
| `negocio/modelos.py` | Negocio | `Habitacion`, `Huesped`, `Reserva` (incluye `se_superpone`). |
| `negocio/errores.py` | Negocio | `ErrorDeNegocio` para rechazos. |
| `datos/repositorio_json.py` | Datos | Lee/escribe el JSON (escritura atómica). |
| `main.pyw` / `main.py` | — | Ensamblan las capas (ventana / consola). |

Dependencias: presentación → negocio → (interfaz de repositorio) ← datos. El negocio no importa nada de presentación ni de datos concretos.
Diagrama: `docs/diagrama_componentes.mermaid`.
