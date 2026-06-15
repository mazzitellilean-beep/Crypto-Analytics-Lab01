# Crypto-Analytics-Lab01
### Sistema de Gestión y Análisis de Activos Digitales

Proyecto desarrollado como trabajo práctico integrador para la materia de Pensamiento Computacional, Algoritmia y Programación en UADE.

---

## ¿Qué hace este sistema?

Crypto-Analytics Lab es una herramienta de consola que permite gestionar un catálogo de activos digitales (criptomonedas, ETFs, acciones tecnológicas, etc.) y una cartera de inversión independiente. A través de un menú interactivo con colores, el usuario puede administrar ambos módulos de forma separada: primero registrar los activos disponibles en el catálogo, y luego gestionar qué activos forman parte de la cartera y en qué cantidades.

---

## Estructura del proyecto

El proyecto está compuesto por tres archivos `.py`:

`main.py` → Punto de entrada del programa. Inicializa el catálogo y la cartera, y ejecuta el loop principal del menú.

`funciones.py` → Contiene toda la lógica del sistema, dividida en cuatro secciones:
- **Front:** funciones que interactúan directamente con el usuario (entrada/salida por consola): `alta_activo`, `alta_activo_catalogo`, `eliminar`, `eliminar_catalogo`, `modificar_activo`, `modificar_activo_catalogo`, `mostrar_matriz`, `mostrar_catalogo`, `ingreso_metodologia`, `volumen_superior_al_promedio`, `volumen_superior_al_promedio_catalogo`
- **Back:** funciones internas sin interacción con el usuario: `busqueda_ticker`, `busqueda_nombre`, `ordenar_matriz`, `ordenar_catalogo`, `activo_en_catalogo`
- **Validaciones:** `validar_nombre`, `validar_ticker`, `validar_valor`, `validar_volumen`, `validar_metodologia`, `validar_unidades`, `validar_unidades_alta`, `validar_puntaje`, `validar_repetidos`, `validar_repetidos_catalogo`, `validar_opcion_repetidos`, `validar_opcion_modificar`, `validar_opcion_modificar_catalogo`
- **Menú:** `menu_principal`, `menu_gestion_catalogo`, `menu_gestion_cartera`, `menu_modificar`, `menu_modificar_catalogo`, `menu_metodologia`, `menu_metodologias_repetidas`, `menu_repetidos`, `verificacion_menu_principal`, `verificacion_menu_catalogo`, `verificacion_menu_cartera`

`tablas.py` → Genera y retorna las dos tablas iniciales con los datos precargados: `tabla_catalogo()` y `tabla_cartera()`.

---

## ¿Cómo se ejecuta?

1. Asegurarse de tener Python instalado (versión 3.x).
2. Descargar o clonar los tres archivos del proyecto en una misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar: `python main.py`
4. El programa mostrará el menú principal y esperará que el usuario ingrese una opción.

---

## Estructura de menús

### Decisión de diseño: menú principal con dos submenús

En la Fase II se rediseñó la navegación del sistema para separar claramente la **gestión del catálogo** de la **gestión de la cartera**. En la Fase I existía un único menú que mezclaba ambas responsabilidades; esto se volvió insostenible cuando se incorporó la regla de que un activo no puede existir en cartera si no está previamente registrado en el catálogo.

La solución adoptada fue un **menú principal** que actúa como punto de entrada y deriva al usuario hacia uno de los dos submenús según lo que necesite hacer:

```
==================================================
  SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB
==================================================
1. Gestión catálogo
2. Gestión cartera
8. Salir
==================================================
```

### Submenú: Gestión de catálogo

Permite administrar el catálogo de activos disponibles para operar. Un activo debe existir aquí antes de poder incorporarse a la cartera.

```
==================================================
  SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB
==================================================
1. Registrar nuevo activo (Alta)
2. Eliminar activo del sistema (Baja)
3. Modificar valoracion o puntaje (Modificacion)
4. Informe General - Visualizacion de los datos
5. Informe Activos con Volumen superior al promedio
8. Salir
==================================================
```

### Submenú: Gestión de cartera

Permite administrar la posición de activos en cartera (unidades en tesorería). Solo se pueden agregar activos que ya estén registrados en el catálogo.

```
==================================================
  SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB
==================================================
1. Registrar nuevo activo (Alta)
2. Eliminar activo del sistema (Baja)
3. Modificar valoracion o puntaje (Modificacion)
4. Informe General - Visualizacion de los datos
5. Informe Activos con Volumen superior al promedio
8. Salir
==================================================
```

---

## Datos de cada activo

### En el catálogo

 `Nombre` → Nombre oficial del activo. Actúa como identificador único; no puede estar vacío ni repetido.

 `Valor de referencia` → Precio en USD. Debe ser mayor o igual a 0.

 `Volumen 24hs` → Dinero operado en el último día. Debe ser mayor o igual a 0.

 `Metodología` → Estrategia de operación recomendada. Debe ser una de las siguientes:
 1. Scalping
 2. Day Trading
 3. Swing Trading
 4. HODL

 `Puntaje de confianza` → Evaluación interna del activo asignada por los analistas. Número entero del 1 al 10. Es una característica del activo: si se modifica en el catálogo, se actualiza automáticamente en la cartera.

### En la cartera

Además de los datos del catálogo (que se heredan al dar de alta en cartera), se agrega:

 `Ticker` → Símbolo corto del activo (ej: BTC). Debe contener entre 3 y 5 caracteres alfabéticos.

 `Unidades en tesorería` → Cantidad del activo en posesión. No puede ser negativa. Se gestiona mediante compras y ventas (ver RF06).

---

## Funcionalidades

### Gestión de catálogo

**Alta de activo en catálogo:** Se ingresan los datos del nuevo activo por teclado. Cada campo se valida con un bucle hasta obtener un valor válido. No se permite registrar dos activos con el mismo nombre. Se pueden agregar varios activos seguidos hasta escribir `fin`.

**Baja de activo del catálogo:** Se busca el activo por nombre. Si el activo tiene unidades en cartera, se eliminan también todas sus posiciones en cartera. Se pueden eliminar varios activos seguidos hasta escribir `fin`.

**Modificación de activo en catálogo:** Se busca el activo por nombre. A través de un submenú se puede modificar el valor de referencia, el volumen, la metodología y el puntaje de confianza. El nombre no puede modificarse ya que actúa como identificador. Los cambios en valor de referencia, volumen y puntaje de confianza se propagan automáticamente a todos los registros de cartera del mismo activo.

**Informe general del catálogo:** Muestra todos los activos en una tabla formateada con columnas alineadas, ordenados por puntaje de confianza de mayor a menor. En caso de empate, se ordenan alfabéticamente por nombre.

**Informe de volumen superior al promedio (catálogo):** Calcula el volumen promedio de todos los activos del catálogo y muestra únicamente aquellos cuyo volumen lo supera, incluyendo la diferencia respecto al promedio. Si ningún activo lo supera, informa la situación.

### Gestión de cartera

**Alta de activo en cartera:** Se ingresa el nombre del activo a incorporar. El sistema verifica que el activo exista en el catálogo antes de continuar; si no existe, lo informa y no permite el alta. Se heredan del catálogo el valor de referencia, el volumen y el puntaje de confianza. No se permite registrar el mismo activo con la misma metodología dos veces.

**Baja de activo de cartera:** Se busca el activo por ticker. Solo se pueden eliminar activos con 0 unidades en tesorería. Si hay múltiples activos con el mismo ticker y 0 unidades, se muestra un menú para elegir por metodología. Se pueden eliminar varios activos seguidos hasta escribir `fin`.

**Modificación de activo en cartera:** Se busca el activo por nombre. Permite modificar el ticker, la metodología y las unidades en tesorería. Si hay múltiples activos con el mismo nombre, se muestra un menú para elegir cuál modificar.

**Actualización de unidades en tesorería (compra/venta):** Desde el submenú de modificación de cartera, se puede ingresar una cantidad de unidades positiva (compra, suma al saldo) o negativa (venta, resta al saldo). El sistema verifica que haya unidades suficientes antes de permitir una venta; si la operación dejaría el saldo en negativo, la rechaza e informa el motivo.

**Informe general de cartera:** Muestra todos los activos de la cartera en una tabla formateada con columnas alineadas, ordenados por puntaje de confianza de mayor a menor. En caso de empate, se ordenan alfabéticamente por nombre.

**Informe de volumen superior al promedio (cartera):** Igual al del catálogo pero calculado sobre los activos en cartera.

### Ingreso de metodología (RF02C)

El ingreso de metodología fue rediseñado para evitar errores. En lugar de ingresar un número, el usuario escribe texto libre (mínimo 3 letras). El sistema:
- Si el texto coincide exactamente con una metodología, la acepta directamente.
- Si coincide parcialmente con una sola metodología, pide confirmación.
- Si coincide parcialmente con varias, muestra las opciones y permite elegir.
- Si no hay coincidencias, informa el error y vuelve a solicitar el dato.

### Colores en la interfaz (RF01)

- **Verde** → títulos de menú y mensajes de operación exitosa.
- **Rojo** → mensajes de error y validaciones fallidas.
- **Amarillo** → solicitudes de ingreso de datos al usuario.

---

## Submenú de modificación de catálogo

```
1. Cambiar valor de referencia
2. Cambiar volumen de actividad
3. Cambiar metodología
4. Cambiar puntaje de confianza (1-10)
5. Salir
```

## Submenú de modificación de cartera

```
1. Cambiar ticker
2. Cambiar metodología de operación
3. Cambiar unidades en tesorería
8. Salir
```

---

## Activos precargados

El sistema inicia con datos de ejemplo cargados desde `tablas.py`:

- **Catálogo (`tabla_catalogo`):** 46 activos disponibles para operar, incluyendo criptomonedas (Bitcoin, Ethereum, Solana, XRP, Cardano, Chainlink, etc.), acciones tecnológicas (Apple, Microsoft, NVIDIA, Tesla, Meta, Adobe, etc.), ETFs (SPY, QQQ, ARKK, GLD, SLV, Vanguard, etc.) y empresas de distintos sectores (salud, energía, finanzas, consumo).

- **Cartera (`tabla_cartera`):** 20 activos en posición, todos presentes también en el catálogo, con sus respectivos tickers y unidades en tesorería.

---

## Autores

Proyecto desarrollado por el **Equipo 01** como parte del trabajo práctico de la materia Programación — Primer año.

`Bejarano, Facundo`

`Cabornero, Santiago`

`Lopez Rubio, Federico`

`Mazzitelli, Leandro`

`Oviedo, Luciano`
