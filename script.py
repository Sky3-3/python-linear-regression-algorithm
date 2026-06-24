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
