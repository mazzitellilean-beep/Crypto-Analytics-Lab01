# Crypto-Analytics-Lab01
### Sistema de Gestión y Análisis de Activos Digitales

---

## Sobre el proyecto

Este repositorio contiene el **Trabajo Práctico Integrador** de la materia **Pensamiento Computacional, Algoritmia y Programación** — UADE, primer año.

El trabajo representa la nota del **segundo parcial** y fue desarrollado en dos fases de entrega iterativas. Está implementado íntegramente en **Python**, sin dependencias externas: solo la biblioteca estándar del lenguaje.

---

## Fases del proyecto

### Fase I — Entrega base

Primera versión funcional del sistema. Implementa las operaciones esenciales de un ABM (alta, baja, modificación) sobre una única lista de activos digitales, con validaciones básicas y un menú de consola.

**Archivos:** `main.py`, `funciones.py`, `tabla_original.py`

Funcionalidades incluidas:
- Alta de activo con validación de campos y control de duplicados.
- Baja por ticker (solo activos con 0 unidades en tesorería).
- Modificación de cualquier campo por nombre del activo.
- Informe general ordenado por puntaje de confianza.

---

### Fase II — Versión final

Versión definitiva del sistema, resultado de aplicar todas las correcciones solicitadas y agregar las nuevas funcionalidades requeridas por la cátedra. Representa la forma final del proyecto.

**Archivos:** `main.py`, `funciones.py`, `tablas.py`

Mejoras técnicas respecto a la Fase I (re-ingeniería):
- Se agregó función `main()` con uso de `if __name__ == "__main__"`.
- Los módulos agrupan múltiples funciones separadas en Front, Back, Validaciones y Menú.
- Todos los imports se ubican al inicio del archivo.
- El programa no puede romperse por entradas inválidas: cada campo se valida en un bucle y la conversión de tipo se realiza solo después de validar el formato.
- Se creó una función de búsqueda independiente (`busqueda_ticker`, `busqueda_nombre`) que es reutilizada por eliminar y modificar.
- Toda función tiene su docstring.
- La función de modificación original (con `continue`) quedó comentada para su análisis en la defensa.

Nuevas funcionalidades (Fase II):
- **Separación catálogo / cartera:** el sistema ahora maneja dos estructuras de datos independientes. El catálogo contiene todos los activos disponibles para operar; la cartera contiene los activos en posesión con sus unidades en tesorería. No se puede dar de alta un activo en cartera si no existe previamente en el catálogo.
- **Menú principal con submenús:** se introdujo un menú principal que deriva hacia el submenú de gestión de catálogo o el de gestión de cartera, separando claramente las responsabilidades de cada módulo.
- **ABM completo del catálogo:** alta, baja y modificación de activos en el catálogo, independiente de las operaciones de cartera.
- **Compra y venta de unidades (RF06):** al modificar un activo en cartera se puede ingresar una cantidad positiva (compra) o negativa (venta). El sistema verifica que haya unidades suficientes antes de ejecutar una venta.
- **Ingreso de metodología por texto (RF02C):** el usuario escribe texto libre (mínimo 3 letras). Si hay coincidencia exacta se acepta; si hay coincidencia parcial se pide confirmación; si hay varias coincidencias se presenta un submenú de selección.
- **Informe de volumen superior al promedio (RF04):** calcula el promedio de volumen operado en 24hs y muestra únicamente los activos que lo superan, con la diferencia individual. Disponible tanto para catálogo como para cartera.
- **Interfaz con colores (RF01):** errores en rojo, títulos y confirmaciones en verde, solicitudes de ingreso en amarillo.
- **Propagación de datos catálogo → cartera:** al modificar el valor de referencia, volumen o puntaje de confianza de un activo en el catálogo, el cambio se refleja automáticamente en todos los registros de cartera del mismo activo.

---

## Requisitos

- Python 3.x
- Sin dependencias externas

---

## Ejecución

Desde la carpeta de la fase correspondiente:

```
python main.py
```

---

## Autores

Proyecto desarrollado por el **Equipo 01**.

`Bejarano, Facundo`

`Cabornero, Santiago`

`Lopez Rubio, Federico`

`Mazzitelli, Leandro`

`Oviedo, Luciano`
