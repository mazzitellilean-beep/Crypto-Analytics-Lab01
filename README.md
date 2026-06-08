# Crypto-Analytics-Lab01
### Sistema de Gestión y Análisis de Activos Digitales

Proyecto desarrollado para la materia de Pnesamiento Computacional, Algoritmia y Programación — Fase 1 (Versión Inicial).

---

## ¿Qué hace este sistema?

Crypto-Analytics Lab es una herramienta de consola que permite gestionar una cartera de activos digitales (criptomonedas, ETFs, acciones tecnológicas, etc.). A través de un menú interactivo, el usuario puede registrar nuevos activos, eliminarlos, modificar sus datos y visualizar un informe ordenado.

---

## Estructura del proyecto

El proyecto está dividido en varios archivos `.py`, cada uno con una responsabilidad específica:

| Archivo | ¿Qué hace? |
|---|---|
| `main.py` | Punto de entrada del programa. Inicializa la tabla y gestiona el ciclo del menú principal. |
| `mostrar_menu.py` | Muestra el menú principal y captura la opción elegida por el usuario. |
| `validacion_opcion.py` | Recibe la opción del menú y llama a la función correspondiente. |
| `generacion_tabla.py` | Genera la tabla inicial con activos precargados. |
| `carga_matriz.py` | Permite registrar nuevos activos ingresando los datos por teclado. Valida Border Cases e imprime el respectivo mensaje de error. |
| `baja_activo.py` | Permite eliminar un activo buscándolo por su ticker. |
| `modificar_activo.py` | Permite modificar los datos de un activo existente buscándolo por nombre. |
| `mostrar_matriz.py` | Muestra todos los activos en formato de tabla ordenada. |
| `ordenar_matriz.py` | Ordena la lista por puntaje de confianza (de mayor a menor) y luego por nombre (alfabéticamente). |

---

## ¿Cómo se ejecuta?

1. Asegurarse de tener Python instalado (versión 3.x).
2. Descargar o clonar todos los archivos del proyecto en una misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar:

```
python main.py
```

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

| Campo | Descripción | Restricciones |
|---|---|---|
| Nombre | Nombre oficial del activo | No puede estar vacío |
| Ticker | Símbolo corto del activo (ej: BTC) | Entre 3 y 5. No puede estar vacio |
| Valor de referencia | Precio en USD | Debe ser mayor a 0 |
| Volumen 24hs | Dinero operado en el último día | No puede ser negativo |
| Metodología | Estrategia de operación asignada | Scalping / Day Trading / Swing Trading / HODL |
| Unidades en tesorería | Cantidad del activo en cartera | No puede ser negativo |
| Puntaje de confianza | Evaluación interna del activo | Número entero del 1 al 10 |

---

## Funcionalidades

**Alta de activo:** Se ingresan los datos del nuevo activo por teclado. El sistema valida cada campo antes de guardarlo. Se pueden agregar varios activos seguidos hasta escribir `fin`.

**Baja de activo:** Se busca el activo por su ticker. Solo se puede eliminar si sus unidades en tesorería son 0. Se puede eliminar varios activos seguidos hasta escribir `fin`.

**Modificación:** Se busca el activo por nombre y se elige qué campo modificar a través de un submenú. Es posible modificar múltiples campos antes de salir.

**Informe general:** Muestra todos los activos en una tabla formateada, ordenados por puntaje de confianza de mayor a menor. En caso de empate en el puntaje, se ordenan alfabéticamente por nombre.

---

## Activos precargados

El sistema inicia con 20 activos de ejemplo que incluyen criptomonedas (Bitcoin, Ethereum, Solana, XRP, BNB), acciones tecnológicas (Apple, Microsoft, NVIDIA, Tesla, Meta) y ETFs (SPY, QQQ, ARKK, GLD, SLV), entre otros.

---

## Autores

Proyecto desarrollado por el **Equipo 01** como parte del trabajo práctico de la materia Programación — Primer año.

Bejarano, Facundo

Cabornero, Santiago

Lopez Rubio, Federico

Mazzitelli, Leandro

Oviedo, Luciano
