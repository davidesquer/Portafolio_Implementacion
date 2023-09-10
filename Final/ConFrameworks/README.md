# Predicción del Costo del Seguro

Esta carpeta contiene modelos de redes neuronales desarrollados para predecir los cargos de seguros basados en varias características de los asegurados.

## Descripción

Este proyecto contiene dos modelos de redes neuronales desarrollados para predecir los cargos de seguros basados en varias características de los asegurados. El primer modelo es una red neuronal de regresión que predice los cargos exactos del seguro para un individuo. El segundo modelo es una red neuronal de clasificación que categoriza los cargos del seguro en bajo, medio o alto.

## Dataset

Para este proyecto se utilizo el dataset de [Insurance](https://experiencia21.tec.mx/courses/406127/files/149437937?module_item_id=24944904), que contiene 1339 ejemplos de las caracteristicas de los asegurados y el costo de su seguro. Cada ejemplo tiene seis características: edad, sexo, indice de masa corporal, numero de hijos, si fuma o no, y la region donde vive.

Variables:

- `age`: La edad del asegurado.
- `sex`: Género del asegurado.
- `bmi`: Índice de Masa Corporal, una medida para determinar la grasa corporal basada en altura y peso.
- `children`: Número de dependientes/hijos cubiertos por el seguro.
- `smoker`: Si el individuo fuma o no.
- `region`: Región geográfica del asegurado.
- `charges`: Los cargos o primas del seguro para el individuo.

Más adelante en el análisis, se introduce una columna `category` para clasificar los cargos de seguro en tres categorías basadas en cuartiles: bajo (0), medio (1) y alto (2).

## Estructura del proyecto

Esta carpeta contiene los siguientes archivos:
- `insurance.csv`: Dataset de Insurance.
- `model.ipynb`: Código que contiene ambas redes neuronales, la de regresión que predice los cargos exactos del seguro y la de clasificación que categoriza los cargos del seguro en bajo, medio o alto.
- `README.md`: Este archivo.
- `machine_learning_con_uso_de_frameworks.pdf`: Reporte formado por la renderizacion del notebook `model.ipynb`, en formato de latex a pdf.

## Archivos a revisar

- `model.ipynb`: Archivo donde se muestra el codigo y explicacion de la utilizacion de los modelos de red neuronal.
- `machine_learning_con_uso_de_frameworks.pdf`: Reporte formado por la renderizacion del notebook `model.ipynb`, en formato de latex a pdf.

## Cambios realizados

- Se agrego al readme la descripcion y fuente del dataset utilizado.
- Se agrego la estructura de como esta formada la carpeta.
- Se agrego lista de los archivos a revisar.
- Se agrego el archivo `machine_learning_con_uso_de_frameworks.pdf` que contiene el reporte formado por la renderizacion del notebook `model.ipynb`, en formato de latex a pdf.
- Se agrego al reporte la informacion y ubicacion del dataset utilizado.
- Se agrego al reporte las descripciones de los 2 modelos de clasificacion y regresion.
- Se agrego al reporte descripciones e interpretaciones de las metricas de desempeño de los modelos.
- Se agregaron 3 predicciones en ambos modelos.

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
