# Crypto-Analytics-Lab01
### Sistema de Gestión y Análisis de Activos Digitales

Proyecto desarrollado como trabajo práctico integrador para la materia de Pensamiento Computacional, Algoritmia y Programación en UADE.

---

## ¿Qué hace este sistema?

Crypto-Analytics Lab es una herramienta de consola que permite gestionar una cartera de activos digitales (criptomonedas, ETFs, acciones tecnológicas, etc.). A través de un menú interactivo, el usuario puede registrar nuevos activos, eliminarlos, modificar sus datos y visualizar un informe ordenado.

---

## Estructura del proyecto

El proyecto está compuesto por tres archivos `.py`:

`main.py` → Punto de entrada del programa. Inicializa la tabla de activos y ejecuta el loop principal del menú.

`funciones.py` → Contiene toda la lógica del sistema, dividida en tres secciones:
- **Front:** `alta_activo`, `eliminar`, `modificar_activo`, `mostrar_matriz`, `menu_modificar`
- **Back:** `busqueda_ticker`, `busqueda_nombre`, `ordenar_matriz`
- **Validaciones:** `validar_nombre`, `validar_ticker`, `validar_valor`, `validar_volumen`, `validar_metodologia`, `validar_unidades`, `validar_puntaje`, `validar_repetidos`
- **Menu:** `menu`, `verificacion_menu`

`tabla_original.py` → Genera y retorna la tabla inicial con los activos precargados.

---

## ¿Cómo se ejecuta?

1. Asegurarse de tener Python instalado (versión 3.x).
2. Descargar o clonar los tres archivos del proyecto en una misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar: `python main.py`
4. El programa mostrará el menú principal y esperará que el usuario ingrese una opción.

---

## Menú principal

```
==================================================
  SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB
==================================================
1. Registrar nuevo activo (Alta)
2. Eliminar activo del sistema (Baja)
3. Modificar valoracion o puntaje (Modificacion)
4. Informe General - Visualizacion de los datos
8. Salir
==================================================
```

---

## Datos de cada activo

Cada activo almacena los siguientes datos:

 `Nombre` -> Nombre oficial del activo. No puede estar vacío 

 `Ticker` -> Símbolo corto del activo (ej: BTC). Entre 3 y 5. No puede estar vacio 

 `Valor de referencia` -> Precio en USD. Debe ser mayor a 0 

 `Volumen 24hs` -> Dinero operado en el último día. No puede ser negativo 

 `Metodología` -> Estrategia de operación asignada. Scalping / Day Trading / Swing Trading / HODL 

 `Unidades en tesorería` -> Cantidad del activo en cartera. No puede ser negativo 

 `Puntaje de confianza` -> Evaluación interna del activo. Número entero del 1 al 10 

 ---

## Funcionalidades

**Alta de activo:** Se ingresan los datos del nuevo activo por teclado. El sistema valida cada campo antes de guardarlo. Se pueden agregar varios activos seguidos hasta escribir `fin`.

**Baja de activo:** Se busca el activo por su ticker. Si hay múltiples activos con el mismo ticker, se solicita al usuario elegir por metodología. Se pueden eliminar varios activos seguidos hasta escribir `fin`.

**Modificación:** Se busca el activo por nombre y se elige qué campo modificar a través de un submenú. Si hay múltiples activos con el mismo nombre, se solicita elegir por metodología. Es posible modificar múltiples campos antes de salir con la opción `8`.

**Informe general:** Muestra todos los activos en una tabla formateada, ordenados por puntaje de confianza de mayor a menor. En caso de empate en el puntaje, se ordenan alfabéticamente por nombre.

---

## Submenú de modificación

```
1. Cambiar nombre del activo
2. Cambiar ticker
3. Cambiar valor de referencia
4. Cambiar volumen de actividad
5. Cambiar metodología de operación
6. Cambiar unidades en tesorería
7. Cambiar puntaje de confianza (1-10)
8. Salir
```

---

## Activos precargados

El sistema inicia con activos de ejemplo cargados desde `tabla_original.py`, que incluyen criptomonedas (Bitcoin, Ethereum, Solana, XRP, BNB), acciones tecnológicas (Apple, Microsoft, NVIDIA, Tesla, Meta) y ETFs (SPY, QQQ, ARKK, GLD, SLV), entre otros.

---

## Autores

Proyecto desarrollado por el **Equipo 01** como parte del trabajo práctico de la materia Programación — Primer año.

`Bejarano, Facundo`

`Cabornero, Santiago`

`Lopez Rubio, Federico`

`Mazzitelli, Leandro`

`Oviedo, Luciano`
