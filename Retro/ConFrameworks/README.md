# Predicción del Costo del Seguro

Esta carpeta contiene modelos de redes neuronales desarrollados para predecir los cargos de seguros basados en varias características de los asegurados.

## Conjunto de Datos

El conjunto de datos, llamado `insurance.csv`, proporciona detalles de varios individuos asegurados y los cargos correspondientes que incurren. El conjunto de datos comprende las siguientes características:

- `age`: La edad del asegurado.
- `sex`: Género del asegurado.
- `bmi`: Índice de Masa Corporal, una medida para determinar la grasa corporal basada en altura y peso.
- `children`: Número de dependientes/hijos cubiertos por el seguro.
- `smoker`: Si el individuo fuma o no.
- `region`: Región geográfica del asegurado.
- `charges`: Los cargos o primas del seguro para el individuo.

Más adelante en el análisis, se introduce una columna `category` para clasificar los cargos de seguro en tres categorías basadas en cuartiles: bajo (0), medio (1) y alto (2).

## Modelos de Red Neuronal

### 1. Red Neuronal de Regresión

Este modelo predice los cargos exactos del seguro para un individuo. La estructura de este modelo es:

- Capa de entrada
- Capa oculta 1: 32 neuronas con activación ReLU
- Capa oculta 2: 16 neuronas con activación ReLU
- Capa de salida: 1 neurona

El modelo utiliza la pérdida de Error Cuadrático Medio (MSE) para el entrenamiento y el optimizador Adam.

### 2. Red Neuronal de Clasificación

Este modelo clasifica los cargos del seguro en tres categorías: bajo, medio y alto. La estructura de este modelo es:

- Capa de entrada
- Capa oculta 1: 32 neuronas con activación ReLU
- Capa oculta 2: 16 neuronas con activación ReLU
- Capa de salida: 3 neuronas con activación Softmax

El modelo utiliza la pérdida de Entropía Cruzada para el entrenamiento y el optimizador Adam.

## Archivos en esta Carpeta

- `insurance.csv`: Conjunto de datos que contiene detalles de los individuos asegurados y los cargos que incurren.
- `model.ipynb`: Código que contiene ambas redes neuronales, la de regresión que predice los cargos exactos del seguro y la de clasificación que categoriza los cargos del seguro en bajo, medio o alto.

