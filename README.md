# Friend-Recommender

Sistema de recomendaciones basado en amigos para redes sociales, implementado en Python usando grafos.

## Descripción

Este proyecto implementa un sistema de recomendaciones inspirado en redes sociales (como Instagram o TikTok), donde las sugerencias se basan en los gustos de amigos cercanos o usuarios relacionados. El sistema utiliza grafos para modelar las relaciones de amistad entre usuarios.

## Características

- **Modelado de red social**: Representación de usuarios y sus relaciones de amistad mediante grafos (usando NetworkX)
- **Gestión de usuarios**: Cada usuario tiene un conjunto de gustos o intereses
- **Cálculo de similitud**: Algoritmo que calcula qué tan similares son dos usuarios basándose en gustos compartidos (coeficiente de Jaccard)
- **Sistema de recomendaciones**: Recomienda intereses populares entre los amigos más cercanos, ponderados por similitud
- **Análisis de red**: Estadísticas sobre la estructura de la red social



## 🔍 Algoritmo de Recomendación

El algoritmo de recomendación funciona de la siguiente manera:

1. **Cálculo de similitud**: Para cada par de usuarios, se calcula la similitud usando el coeficiente de Jaccard:
   ```
   similitud = (gustos_compartidos) / (gustos_totales_únicos)
   ```

2. **Ordenamiento de amigos**: Los amigos se ordenan por similitud (de mayor a menor)

3. **Ponderación de gustos**: Los gustos de los amigos se ponderan por su similitud con el usuario objetivo

4. **Filtrado**: Se excluyen los gustos que el usuario ya tiene

5. **Ranking**: Los intereses se ordenan por score (suma ponderada de similitudes) y se retornan los mejores


## Notas

- El sistema utiliza grafos no dirigidos para representar amistades (si A es amigo de B, entonces B es amigo de A)
- La similitud se calcula usando el coeficiente de Jaccard, que es una métrica estándar para comparar conjuntos
- Las recomendaciones están ponderadas por similitud, dando más peso a los gustos de amigos más similares

## Dependencias

- `networkx`: Librería para trabajar con grafos en Python

