# Portafolio de implementacion

Esta carpeta contiene 2 proyectos de implementacion de modelos de machine learning y deep learning, ademas de estos 2 se le agrego un nuevo proyecto de construccion de un modelo estadistico base.

## Proyectos

### 1. Implementacion de un modelo de regresion logisitica multiple sin la utilizacion de un framework de machine learning
Este proyecto corresponde a la carpeta `SinFramework`.

La regresión logística es un método estadístico para modelar relaciones entre una variable dependiente binaria y una o más variables independientes. Este código es específico para la regresión logística binaria, lo que significa que se predice entre dos clases posibles.

#### Archivos en esta Carpeta

- `iris.csv`: Conjunto de datos iris.
- `ML_sin_framework.ipynb`: Notebook con la implementacion del modelo de regresion logistica multiple sin la utilizacion de un framework de machine learning.

### 2. Implementacion de un modelo de clasificacion de seguros utilizando el framework de deep learning pytorch
Este proyecto corresponde a la carpeta `ConFramework`.

En este proyecto se hacen 2 implementaciones de redes neuronales utilizando el framework de deep learning pytorch, una para la regresion de los costos de los seguros y despues otra para clasificar si el costo es bajo, medio o alto.

#### Archivos en esta Carpeta

- `insurance.csv`: Conjunto de datos que contiene detalles de los individuos asegurados y los cargos que incurren.
- `model.ipynb`: Código que contiene ambas redes neuronales, la de regresión que predice los cargos exactos del seguro y la de clasificación que categoriza los cargos del seguro en bajo, medio o alto.

### 3. Implementacion de un modelo estadistico base.
Este proyecto corresponde a la carpeta `EstadisticoBase`.

#### Archivos en esta Carpeta

- `autos_prepared.csv`: Conjunto de datos que contiene detalles de los autos y sus precios, ya preparado para el modelo estadistico.
- `modelacion.ipynb`: Código que contiene el modelo estadistico base.