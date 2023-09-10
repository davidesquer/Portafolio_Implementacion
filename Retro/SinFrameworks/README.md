# Regresión Logística en Python

Este proyecto proporciona una implementación simple de regresión logística en Python sin depender de bibliotecas externas como numpy o scikit-learn.

## Descripción

La regresión logística es un método estadístico para modelar relaciones entre una variable dependiente binaria y una o más variables independientes. Este código es específico para la regresión logística binaria, lo que significa que se predice entre dos clases posibles.

## Funcionamiento

El código se compone de varias funciones:

- `sigmoide(z)`: Calcula la función sigmoide, que convierte un número real en un valor entre 0 y 1.
- `calcular_costo(X, y, theta)`: Calcula el costo de los parámetros actuales `theta` usando la función de costo logarítmico.
- `entrenar_regresion_logistica(X, y, alpha=0.01, num_iteraciones=1000)`: Entrena el modelo de regresión logística utilizando el algoritmo de descenso del gradiente.
- `predecir(X, theta)`: Usa el modelo entrenado (los parámetros `theta`) para predecir las clases de nuevos ejemplos.