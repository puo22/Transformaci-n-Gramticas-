# 📘Analizador Sintáctico Descendente Recursivo (ASDR) 
---
### Ejercicios 1, 2 y 3 — Presentación 7  

Este proyecto implementa **analizadores sintácticos descendentes recursivos (ASDR)** en **Python**, para tres gramáticas diferentes, cada una almacenada en su propio conjunto de archivos.  

Cada analizador carga su **gramática desde un archivo `.txt`**, procesa **tokens definidos por el usuario**, y muestra paso a paso la **derivación sintáctica**, indicando los **emparejamientos exitosos** y los **errores** si ocurren.  

---

## 📂 Estructura del Proyecto

```

asdr-ejercicios/
│
├── ejercicio1/
│   ├── gramatica.txt
│   ├── tokens.py
│   ├── gramatica_parser.py
│   ├── analizador.py
│   ├── pruebas.py
│   └── main.py
│
├── ejercicio2/
│   ├── gramatica.txt
│   ├── tokens.py
│   ├── gramatica_parser.py
│   ├── analizador.py
│   ├── pruebas.py
│   └── main.py
│
└── ejercicio3/
├── gramatica.txt
├── tokens.py
├── gramatica_parser.py
├── analizador.py
├── pruebas.py
└── main.py

```

Cada carpeta contiene todo lo necesario para ejecutar el ASDR del ejercicio correspondiente.  

---

## Requisitos

- **Python 3.8+**
- No requiere librerías externas (solo la librería estándar)

---

## Ejecución

Cada ejercicio se ejecuta de forma independiente.

### Para ejecutar un ejercicio:
1. Abre la terminal en la carpeta del ejercicio (por ejemplo, `ejercicio1/`).
2. Ejecuta el comando:

```bash
python3 main.py
````

3. El programa cargará automáticamente la gramática desde `gramatica.txt`, mostrará las producciones y luego ejecutará una **serie de pruebas** definidas en `pruebas.py`.

4. Presiona **Enter** entre cada prueba para continuar, o **Ctrl+C** para detener el proceso.

---

## Descripción de Archivos

| Archivo                 | Descripción                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **gramatica.txt**       | Contiene las reglas de producción de la gramática libre de contexto para cada ejercicio.                         |
| **tokens.py**           | Define los símbolos terminales (tokens) que el analizador reconoce.                                              |
| **gramatica_parser.py** | Carga y muestra la gramática desde el archivo `.txt`.                                                            |
| **analizador.py**       | Implementa el **ASDR**: funciones recursivas para cada no terminal. Incluye emparejamiento y control de errores. |
| **pruebas.py**          | Define las cadenas de prueba que el analizador ejecuta automáticamente.                                          |
| **main.py**             | Punto de entrada del programa. Carga la gramática, ejecuta el analizador y muestra los resultados.               |

---

## Ejercicios Incluidos

### **Ejercicio 1**

**Objetivo:** Eliminar recursión por la izquierda y construir el ASDR.
**Características:**

* Gramática transformada (sin recursión izquierda).
* Carga dinámica de la gramática.
* Reconoce estructuras con los tokens `uno`, `dos`, `tres`, `cuatro`, `cinco`, `seis`.
* Incluye 5 pruebas con combinaciones válidas e inválidas.

📄 **Archivo principal:** `ejercicio1/main.py`

---

### **Ejercicio 2**

**Objetivo:** Implementar el ASDR y verificar si la gramática es LL(1).
**Características:**

* Incluye epsilon-producciones.
* Reconoce tokens `uno`, `dos`, `tres`, `cuatro`, `cinco`, `seis`, `siete`.
* Muestra la gramática cargada y el proceso de derivación.

📄 **Archivo principal:** `ejercicio2/main.py`

---

### **Ejercicio 3**

**Objetivo:** Eliminar recursividad por la izquierda y construir el ASDR correspondiente.
**Características:**

* Usa un nuevo símbolo auxiliar `S'` para eliminar recursión.
* Gramática simplificada para derivaciones con `uno`, `dos`, `tres`, `cuatro`.
* Incluye derivaciones con y sin epsilon.

📄 **Archivo principal:** `ejercicio3/main.py`

---

## 🔍 Ejemplo de Salida

```bash
══════════════════════════════════════════════════════════════════
  Prueba 1: dos tres
══════════════════════════════════════════════════════════════════

============================================================
    ANALIZADOR EJERCICIO 1
============================================================
Entrada: dos tres $

GRAMÁTICA CARGADA
S → A B C
S → D E
A → dos B tres
A → ε
B → ε B'
B' → cuatro C cinco B'
B' → ε
C → seis A B
C → ε
D → uno A E
D → B
E → tres

→ S con token: 'dos'
  S → A B C
    → A con token: 'dos'
      A → dos B tres
      ✓ Emparejado: dos
      ...
✓ ANÁLISIS EXITOSO
============================================================
```

---

## Conceptos Clave

* **ASDR (Análisis Sintáctico Descendente Recursivo):**
  Técnica de análisis sintáctico basada en la construcción de un conjunto de funciones recursivas (una por cada no terminal).
  Las decisiones se toman con base en los conjuntos **FIRST** y **FOLLOW**.

* **Eliminación de Recursividad por la Izquierda:**
  Reescritura de reglas del tipo `A → A α | β` en una forma equivalente `A → β A'` y `A' → α A' | ε`.

* **Gramáticas LL(1):**
  Aquellas que pueden analizarse mirando solo **1 token de anticipación** sin ambigüedad.

---

## Pruebas Incluidas

Cada `pruebas.py` incluye varias cadenas de entrada (válidas e inválidas) para verificar el comportamiento del analizador.
Ejemplos:

* `"uno tres $"`
* `"dos seis tres $"`
* `"cuatro tres uno $"`
* `"$"` (cadena vacía)

El analizador imprime paso a paso los **no terminales invocados**, los **tokens emparejados** y los **errores encontrados**.

---

## 👨‍💻 Autor

**Paula Alejandra Ortiz Salon**



