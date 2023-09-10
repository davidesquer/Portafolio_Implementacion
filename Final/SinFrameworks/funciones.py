import numpy as np

def sigmoide(z):
    return 1.0 / (1.0 + np.exp(-z))

def calcular_costo(X, y, theta):
    m = len(y)
    h = sigmoide(X @ theta)
    costo = (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    return costo

def entrenar_regresion_logistica(X, y, alpha, num_iteraciones):
    m, n = X.shape
    theta = np.zeros(n)

    for iteracion in range(num_iteraciones):
        h = sigmoide(X @ theta)
        gradiente = (X.T @ (h - y)) / m
        theta -= alpha * gradiente

    return theta

def predecir(X, theta):
    return sigmoide(X @ theta)

def evaluar(X, y, thetas):
    predicciones = predecir_ovr(X, thetas)
    correctas = (predicciones == y).sum()
    return correctas / len(y)

def entrenar_ovr(X, y, clase_actual, alpha, num_iteraciones):
    y_binaria = np.where(y == clase_actual, 1, 0)
    return entrenar_regresion_logistica(X, y_binaria, alpha, num_iteraciones)

def predecir_ovr(X, thetas):
    probabilidades = np.array([predecir(X, theta) for theta in thetas])
    return np.argmax(probabilidades, axis=0)