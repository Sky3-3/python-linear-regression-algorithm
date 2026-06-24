# Proyecto Python: Implementación Algorítmica de Regresión Lineal y Optimización de Pérdida

Este repositorio contiene un proyecto práctico desarrollado en Python enfocado en el modelado de funciones matemáticas para el cálculo de regresiones lineales sin el uso de librerías externas. El script implementa la fórmula clásica de la línea recta para realizar predicciones, calcula el error absoluto acumulado (*Loss Function*) frente a un conjunto de datos coordenados, y ejecuta un algoritmo de fuerza bruta sobre un espacio de búsqueda continuo para hallar los parámetros óptimos de pendiente e intersección.

---

## Código Python del Proyecto

El programa provee las funciones necesarias para calcular los valores estimados de la variable dependiente, medir las desviaciones verticales absolutas y realizar la optimización iterativa del modelo:

```python
# --- 1. Definición de la Recta Proyectada ---
# Calcula el valor de 'y' en la ecuación lineal clásica: y = m*x + b
def get_y(m, x, b):
    y = m * x + b
    return y

# --- 2. Función de Pérdida / Cálculo de Error Unitario ---
# Mide la distancia absoluta (error) entre un punto cartesiano real (x, y) y la recta predictiva
def calculate_error(m, b, point):
    x_point, y_point = point
    y_predicted = get_y(m, x_point, b)
    distance = abs(y_predicted - y_point)
    return distance

# --- 3. Acumulación Global de Error ---
# Calcula la sumatoria del error total sobre todo el conjunto de datos de prueba
def calculate_all_error(m, b, points):
    total_errors = 0
    for point in points:
        total_errors += calculate_error(m, b, point)
    return total_errors

# --- 4. Inicialización del Espacio de Búsqueda Continuo ---
possible_ms = [m / 10 for m in range(-100, 101)]  # Rangos de -10.0 a 10.0 en intervalos de 0.1
possible_bs = [b / 10 for b in range(-200, 201)]  # Rangos de -20.0 a 20.0 en intervalos de 0.1

# Dataset de experimentación (Nube de puntos de rebote)
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

smallest_error = float("inf")
best_m = 0
best_b = 0

# --- 5. Algoritmo de Optimización por Fuerza Bruta (Grid Search) ---
for m in possible_ms:
    for b in possible_bs:
        error_sm = calculate_all_error(m, b, datapoints)
        if error_sm < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error_sm
    
# Impresión formal de los hiperparámetros óptimos calculados
print("Parámetros de Mejor Ajuste:")
print("Pendiente (m): " + str(best_m))
print("Intersección (b): " + str(best_b))
print("Mínimo Error Absoluto Acumulado: " + str(smallest_error))

# Predicción final con el modelo optimizado
print("Predicción para x=1.6: " + str(get_y(best_m, 1.6, best_b)))

```

---

## Análisis Matemático del Algoritmo

El script modela el comportamiento de una regresión lineal simple cuyo modelo matemático responde a la ecuación lineal de la recta:

$$y = m \cdot x + b$$

El objetivo principal es encontrar la **línea de mejor ajuste**, definida como aquella combinación de parámetros de pendiente ($m$) e intersección ($b$) que minimiza de forma global la sumatoria de las distancias verticales de los puntos hacia la recta.

### Estado del Set de Datos y Desviaciones

El script evalúa el dataset `[(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]` barriendo miles de combinaciones en bucles anidados. Tras finalizar las iteraciones del espacio de estados, el motor determina los siguientes valores óptimos:

| Parámetro Calculado | Valor Óptimo | Significado Físico / Geométrico |
| --- | --- | --- |
| **Pendiente ($m$)** | `0.4` | Indica que por cada unidad que avanza la variable $x$, la variable $y$ incrementa en $0.4$. |
| **Intersección ($b$)** | `1.6` | Representa el punto de corte donde la recta intercepta el eje vertical de las ordenadas ($x=0$). |
| **Error Mínimo Acumulado** | `5.0` | La menor suma posible de errores absolutos para este conjunto de datos. |

---

## Conceptos Técnicos Aplicados

* **Ajuste de Rejilla por Fuerza Bruta (*Grid Search*)**: Técnica de optimización que consiste en recorrer un espacio de parámetros previamente definido de forma exhaustiva en bucles anidados para evaluar el rendimiento de cada combinación y seleccionar el mínimo global absoluto.
* **Función de Pérdida Absoluta (*L1 Loss*)**: Modelo estadístico que evalúa el error utilizando el valor absoluto de la diferencia ($|y_{real} - y_{predicho}|$). Al omitir elevar los errores al cuadrado (a diferencia de *L2 Loss / MSE*), reduce la sensibilidad extrema del modelo ante la presencia de datos atípicos (*outliers*).
* **Flotante Infinito (`float("inf")`)**: Valor de control utilizado como umbral inicial para la variable de comparación de mínimos. Al garantizar que cualquier número real calculado sea menor que el infinito, asegura la correcta asignación del primer error procesado por la estructura condicional.

```
