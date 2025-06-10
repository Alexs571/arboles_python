# Implementación de un Árbol Genealógico en Python

Este repositorio contiene el trabajo práctico de la materia **Programación I** titulado **"Implementación de un Árbol Genealógico en Python: Aplicación de Estructuras de Datos Jerárquicas"**.

## Autores
- Diana Cecilia Den Dauw - ceciliadendauw@gmail.com
- Alexis Da Silva - alexis.da.silva.571@gmail.com

## Profesor/a
- Ariel Enferrel

## Fecha de entrega
- 09/06/2025

---

## Índice

1. [Introducción](#1-introducción)
2. [Marco Teórico](#2-marco-teórico)
3. [Caso Práctico](#3-caso-práctico)
4. [Metodología Utilizada](#4-metodología-utilizada)
5. [Resultados Obtenidos](#5-resultados-obtenidos)
6. [Conclusiones](#6-conclusiones)
7. [Bibliografía](#7-bibliografía)
8. [Anexos](#8-anexos)

---

## 1. Introducción

El presente trabajo integra el desarrollo de un árbol genealógico implementado en Python, elegido por la relevancia de las estructuras de datos jerárquicas en programación y su aplicación en diversas áreas como representación de relaciones familiares, organización de carpetas y árboles de decisión.

Se busca fortalecer las competencias en clases, listas y recursividad, integrando conceptos teóricos y prácticos esenciales para programadores.

---

## 2. Marco Teórico

Un árbol es una estructura de datos jerárquica compuesta por nodos conectados mediante relaciones padre-hijo.

### Tipos de árboles:
- **Árbol general**: cada nodo puede tener múltiples hijos. (Implementado en este trabajo)
- **Árbol binario**: cada nodo puede tener como máximo dos hijos.
- **Árbol balanceado**: diferencia de altura entre subárboles no mayor a uno.
- **Árbol completo**: todos los niveles completos, excepto el último, llenado de izquierda a derecha.

### Jerarquía de un árbol genealógico:
- **Raíz**: antepasado principal (Juan Pérez).
- **Niveles intermedios**: generaciones de descendientes.
- **Hojas**: descendientes más jóvenes sin hijos registrados.

---

## 3. Caso Práctico

### Problema a resolver
Modelar un árbol genealógico sencillo en Python que permita representar relaciones familiares. El usuario ingresa un nombre y el programa muestra toda su descendencia de manera jerárquica.

### Decisiones de diseño
- Uso de clases y listas para representar jerarquías.
- Búsqueda en profundidad (DFS) para recorrer y localizar descendientes.
- Impresión recursiva con guiones para representar la jerarquía.

### Validación
Se realizaron pruebas para:
- Buscar a la persona raíz (Juan Pérez) y mostrar descendencia.
- Buscar niveles intermedios como María López y Luis Pérez.
- Comprobar insensibilidad a mayúsculas y minúsculas.
- Mostrar mensaje de error al buscar personas inexistentes.

---

## 4. Metodología Utilizada

- **Investigación previa**: documentación oficial de Python y mejores prácticas de estructuras de datos jerárquicas.
- **Diseño del árbol**: altura 5 con nodos completos (2 hijos por nodo).
- **Codificación y pruebas**:
  - Clase `Nodo` para representar cada persona.
  - Funciones recursivas para búsqueda e impresión jerárquica.
  - Validación con diferentes casos de prueba.

### Herramientas utilizadas
- **IDE**: Visual Studio Code y Notepad++.
- **Lenguaje**: Python 3.x.
- **Control de versiones**: Git (opcional).
- **Terminal**: consola de comandos para pruebas.

### Trabajo colaborativo
- Alexis: investigación y documentación.
- Cecilia: diseño del árbol y planificación.
- Ambos: desarrollo, pruebas y documentación.

---

## 5. Resultados Obtenidos

- Implementación exitosa de un árbol genealógico de altura 5.
- Búsqueda recursiva (DFS) funcional para localizar descendientes.
- Impresión jerárquica clara y ordenada.
- Validación de:
  - Búsquedas en todos los niveles.
  - Nombres inexistentes.
  - Insensibilidad a mayúsculas y minúsculas.

---

## 6. Conclusiones

- Se consolidaron conocimientos de árboles jerárquicos y recursividad en Python.
- Se comprendió la importancia de modelar relaciones jerárquicas en programación.
- Posibles mejoras:
  - Búsqueda de ancestros.
  - Exportación gráfica.
  - Interfaz interactiva.
- Se resolvió la dificultad de mantener la estructura equilibrada a través de planificación y asignación clara de hijos.

---

## 7. Bibliografía

- Python Software Foundation. (2024). [Python 3 Documentation](https://docs.python.org/3/) (acceso: 09/06/2025).
- Sweigart, A. (2019). *Automate the Boring Stuff with Python*. No Starch Press.
- McKinney, W. (2018). *Python for Data Analysis*. O'Reilly Media.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3ra ed.). MIT Press.
- Universidad Nacional del Litoral. (s.f.). Material de apoyo de Programación I.

---

## 8. Anexos

- Capturas del programa funcionando:
  - Descendencia completa.
  - Niveles intermedios.
  - Pruebas con mayúsculas y minúsculas.
  - Búsquedas de personas inexistentes.

---
