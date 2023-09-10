# Regresión Logística en Python

Este proyecto proporciona una implementación simple de regresión logística en Python sin depender de bibliotecas externas como numpy o scikit-learn.

## Descripción

La regresión logística es un método estadístico para modelar relaciones entre una variable dependiente binaria y una o más variables independientes. Este código es específico para la regresión logística binaria, lo que significa que se predice entre dos clases posibles.

## Dataset

Para este proyecto se utilizo el dataset de [Iris](https://www.kaggle.com/datasets/uciml/iris), que contiene 150 ejemplos de flores de tres especies diferentes: Iris Setosa, Iris Versicolour e Iris Virginica. Cada ejemplo tiene cuatro características: longitud del sépalo, ancho del sépalo, longitud del pétalo y ancho del pétalo.

## Estructura del proyecto

Esta carpeta contiene los siguientes archivos:
- `iris.csv`: Dataset de Iris.
- `ML_sin_framework.ipynb`: Implementación de regresión logística sin la utilizacion de un framework.
- `README.md`: Este archivo.
- `funciones.py`: Contiene las funciones necesarias para la implementacion de la regresion logistica.
- `machine_learning_sin_uso_de_frameworks.pdf`: reporte formado por la renderizacion del notebook `ML_sin_framework.ipynb`, en formato de latex a pdf.

## Archivos a revisar

- `ML_sin_framework.ipynb`: Archivo donde se muestra el codigo y explicacion de la utilizacion del modelo de regresion logistica.
- `machine_learning_sin_uso_de_frameworks.pdf`: Reporte formado por la renderizacion del notebook `ML_sin_framework.ipynb`, en formato de latex a pdf.
- `funciones.py`: Contiene las funciones necesarias para la implementacion de la regresion logistica.

## Cambios realizados

- Se agrego al readme la descripcion y fuente del dataset utilizado.
- Se agrego la estructura de como esta formada la carpeta.
- Se agrego el archivo `funciones.py` que contiene las funciones necesarias para la implementacion de la regresion logistica.
- Se realizo el cambio en la implementacion de la regresion logistica para que se utilicen las funciones del archivo `funciones.py`, y en estas funciones se agrego la capacidad de utilizar regresion lineal multiple para que se ajuste a los datos que estabamos utilizando.
- Se agrego el archivo `machine_learning_sin_uso_de_frameworks.pdf` que contiene el reporte formado por la renderizacion del notebook `ML_sin_framework.ipynb`, en formato de latex a pdf.

## Explicación de las Funciones de Regresión Logística Multiclase

#### 1. `sigmoide(z)`

**Función**: Esta función calcula la función sigmoide, que es esencial en la regresión logística.

**Parámetros**:
- `z`: Un número o array.

**Retorno**: Retorna un número entre 0 y 1, que representa la probabilidad.

**Explicación**: La función sigmoide es una función en forma de "S" que convierte un número real en un valor entre 0 y 1. Es comúnmente utilizada para convertir la salida lineal de un modelo en una probabilidad.

#### 2. `calcular_costo(X, y, theta)`

**Función**: Calcula el costo o pérdida de un modelo de regresión logística.

**Parámetros**:
- `X`: Matriz de características.
- `y`: Vector de etiquetas.
- `theta`: Vector de parámetros.

**Retorno**: Un número que representa el costo.

**Explicación**: Esta función calcula el costo utilizando la función de costo logarítmico. Es una medida de cuán bien (o mal) el modelo está prediciendo las etiquetas verdaderas.

#### 3. `entrenar_regresion_logistica(X, y, alpha, num_iteraciones)`

**Función**: Entrena un modelo de regresión logística utilizando el algoritmo de descenso del gradiente.

**Parámetros**:
- `X`: Matriz de características.
- `y`: Vector de etiquetas.
- `alpha`: Tasa de aprendizaje.
- `num_iteraciones`: Número de iteraciones para el descenso del gradiente.

**Retorno**: `theta`, que son los parámetros óptimos del modelo.

**Explicación**: El descenso del gradiente es un algoritmo de optimización utilizado para minimizar el costo y encontrar los parámetros óptimos (`theta`). La tasa de aprendizaje (`alpha`) controla cuán grandes son los pasos durante el descenso.

#### 4. `predecir(X, theta)`

**Función**: Predice las etiquetas de un conjunto de datos.

**Parámetros**:
- `X`: Matriz de características.
- `theta`: Parámetros del modelo.

**Retorno**: Las probabilidades predichas para cada ejemplo en `X`.

**Explicación**: Esta función toma los datos de entrada y los parámetros del modelo, y produce una probabilidad para cada ejemplo utilizando la función sigmoide.

#### 5. `evaluar(X, y, thetas)`

**Función**: Evalúa el rendimiento del modelo en un conjunto de datos.

**Parámetros**:
- `X`: Matriz de características.
- `y`: Vector de etiquetas verdaderas.
- `thetas`: Parámetros del modelo para cada clase.

**Retorno**: La proporción de predicciones correctas.

**Explicación**: Esta función compara las predicciones del modelo con las etiquetas verdaderas y calcula la exactitud.

#### 6. `entrenar_ovr(X, y, clase_actual, alpha, num_iteraciones)`

**Función**: Entrena un clasificador binario para una clase específica contra todas las demás.

**Parámetros**:
- `X`: Matriz de características.
- `y`: Vector de etiquetas.
- `clase_actual`: La clase que se está considerando como positiva.
- `alpha`: Tasa de aprendizaje.
- `num_iteraciones`: Número de iteraciones para el descenso del gradiente.

**Retorno**: Los parámetros `theta` para el clasificador de la `clase_actual`.

**Explicación**: Esta función convierte el problema multiclase en varios problemas binarios utilizando el enfoque One-vs-All (OvA).

#### 7. `predecir_ovr(X, thetas)`

**Función**: Realiza predicciones multiclase utilizando el enfoque OvA.

**Parámetros**:
- `X`: Matriz de características.
- `thetas`: Lista de parámetros para cada clasificador binario.

**Retorno**: Las clases predichas para cada ejemplo en `X`.

**Explicación**: Utiliza cada clasificador binario para hacer una predicción y elige la clase con la mayor probabilidad.
