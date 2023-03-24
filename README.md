# Taller Algoritmos Dinamicos
Santiagos @ Post produccion corregir esto V:
## Objetivo

Escribir tres algoritmos (evidente recursivo, memoizado y bottom-up) asociados a un diseño de un problema que se puede resolver
usando la estrategia de programación dinámica.

## Subsecuencia de producto máxima
El desarrollo del taller consistirá en analizar tres algoritmos asociados al problema de encontrar para una secuencia de
elementos X = ⟨x1, . . . , xn⟩, xi ∈ R la subsecuencia de elementos contiguos cuyo producto es máximo.

Por ejemplo, para la subsecuencia ejemplo X = ⟨−7, 12, −7, 0, 14, −7, 5⟩, la subsecuencia contigua de elementos contiguos
cuyo producto es máximo es X[1 : 3]

## Análisis y diseño del problema

El problema consiste en encontrar una subsecuencia de elementos contiguos dentro de una secuencia dada, cuyo producto sea máximo. Para resolver este problema, se pueden utilizar tres algoritmos asociados a la estrategia de programación dinámica: recursivo, memoizado y bottom-up.

Este problema se puede abordar mediante el uso de un algoritmo eficiente que recorra la secuencia y calcule el producto acumulado de cada subsecuencia, para luego compararlas y encontrar la subsecuencia con el mayor producto. Sin embargo, debido a que hay un número infinito de subsecuencias posibles en una secuencia de longitud n, se necesitará un enfoque más eficiente para resolver este problema.

### Diseño

Entrada: Una secuencia X = ⟨x1, . . . , xn⟩, xi ∈ R .

Salida: Una sub-secuencia Xsub = ⟨xa, . . . , xb⟩, xj ∈ R donde los elementos contiguos son el producto maximo de la secuencia X.