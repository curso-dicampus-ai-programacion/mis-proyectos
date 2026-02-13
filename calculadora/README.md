# 🧮 Calculadora en Python con Tkinter (Tema Oscuro)

## 📌 Descripción

Este proyecto consiste en una **calculadora gráfica desarrollada en Python** utilizando la librería estándar **Tkinter**.

La aplicación simula el comportamiento de una calculadora básica similar a la de Windows, incluyendo:

- Operaciones matemáticas básicas
- Botón de retroceso (⌫)
- Eliminación de decimales innecesarios
- Interfaz con tema oscuro
- Control de errores (como división por cero)

---

## 🚀 Características

### 🔢 Operaciones disponibles

- ➕ Suma
- ➖ Resta
- ✖ Multiplicación
- ➗ División
- % Módulo
- ^ Potencia

---

### 🎨 Interfaz

- Interfaz por linea de comandos `app.py`.
- Interfaz gráfica `app_gui.py`.
- Tema oscuro moderno
- Botones organizados en cuadrícula
- Colores diferenciados por tipo de botón:
  - Números
  - Operadores
  - Igual (=)
  - Limpiar (C)
  - Retroceso (⌫)

---

## 🧠 Funcionamiento Interno

### 1️⃣ Funciones Matemáticas

Se definen funciones independientes para cada operación:

```python
def add(num1, num2):
def subtract(num1, num2):
def multiply(num1, num2):
def divide(num1, num2):
def modulus(num1, num2):
def power(num1, num2):
```

Esto permite mantener una estructura modular y clara.

---

### 2️⃣ Manejo del Estado

La calculadora utiliza variables globales para controlar el flujo:

```python
current_input  # Número que el usuario está escribiendo
first_number   # Primer operando
operation      # Operación seleccionada
```

---

### 3️⃣ Control de Decimales

Por defecto, se utilizan números enteros, pero en caso de que el resultado de un valor con decimales, por ejemplo en una división, se muestran. En caso contrario el resultado se muestra sin decimales. Se utiliza la siguiente funcion para formatear el resultado:

```python
def format_result(result):
```

Elimina decimales innecesarios.

Ejemplo:

- 5.0 → 5
- 5.5 → 5.5

Esto mejora la presentación del resultado.

---

### 4️⃣ Botón de Retroceso (⌫)

```python
def backspace():
```

Elimina el último carácter ingresado, simulando la tecla de retroceso.

---

### 5️⃣ Actualización de Pantalla

```python
def update_display(value):
```

Se encarga de:

- Limpiar el contenido anterior
- Mostrar el nuevo valor en el campo de texto

---

## 🖥️ Interfaz Gráfica

- Construida con `tk.Tk()`
- Botones organizados con `grid()`
- Pantalla implementada con `tk.Entry`
- Diseño fijo: `322x425`
- Ventana no redimensionable

---

## 🛠️ Requisitos

- Python 3.x
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

Para ejecutar:

```bash
python app.py
```

```bash
python app_gui.py
```

---

## 📂 Estructura del Código

El código fuente del archivo `app.py` se ha separado en varias secciones para mejorar la legibilidad. 

```
├── Funciones matemáticas
├── Lógica de la calculadora
│   ├── Entrada de números
│   ├── Selección de operación
│   ├── Cálculo de resultado
│   ├── Limpiar
│   └── Retroceso
├── Configuración de la interfaz
└── Bucle principal (mainloop)
```

---

## ⚠️ Manejo de Errores

- División entre cero devuelve `"Error"`
- No permite múltiples puntos decimales en un número
- Limpia correctamente el estado tras cada operación

---

## 🔮 Posibles Mejoras Futuras

- Soporte para teclado físico
- Operaciones encadenadas sin presionar "="
- Historial de operaciones
- Ajuste automático del tamaño del texto
- Diseño más avanzado con `ttk` o `customtkinter`

---

## 🎯 Contribuir

Para poder contribuir a este proyecto educativo, puedes hacerlo enviando una `pull request` al repositorio con tus cambios.

---

## 📜 Licencia

Proyecto educativo de práctica en Python y Tkinter, licenciado con GNU General Public License (GPL3).
