# Práctica 1: Migración y Cobertura de Código

Este repositorio contiene el desarrollo de la Práctica 1 de la asignatura **Calidad, Pruebas y Mantenimiento del Software**. El objetivo principal es migrar un código heredado desde un entorno legacy (C) a un entorno moderno (Python), asegurando la calidad mediante pruebas automatizadas y un control de versiones estructurado.

## 📋 Descripción del Proyecto

El proyecto consta de tres fases principales:

1. **Entorno Heredado (C)**: Análisis de cobertura de una aplicación escrita en C para la clasificación de triángulos.
2. **Migración a Python**: Traducción de la lógica a Python, manteniendo la funcionalidad original (incluyendo errores detectados).
3. **Corrección y Cobertura**: Identificación de bugs, corrección mediante ramas (`fix/isosceles-logic`) y ampliación de los casos de prueba para alcanzar el 100% de cobertura de código.

## 🚀 Estructura del Repositorio

- `triangulo.c`: Código fuente original en C.
- `triangulo.py`: Código migrado a Python con la lógica corregida.
- `test_triangulo.py`: Suite de pruebas automatizadas utilizando `pytest`.
- `respuestas_memoria.txt`: Documentación con las respuestas a las preguntas planteadas en el enunciado.

## 🛠️ Requisitos Previos

Para ejecutar este proyecto necesitarás:

- **Python 3.x**
- **Librerías de Python**:
  ```bash
  pip install pytest pytest-cov
  ```
- **Extensión VS Code**: "Coverage Gutters".

## ▶️ Ejecución de las Pruebas

Para ejecutar las pruebas y generar el informe de cobertura XML compatible con herramientas de visualización:

```bash
pytest --cov=. --cov-report=xml
```

Esto ejecutará los 9 casos de prueba diseñados, cubriendo:

- Triángulos Equiláteros, Isósceles y Escalenos.
- Condiciones de no-triángulo (desigualdad triangular).
- Casos límite y corrección de bugs específicos (ej. Isósceles `a==c`).

## 🔄 Flujo de Trabajo (Git)

El desarrollo ha seguido un flujo basado en ramas:

- `main`: Contiene la versión estable y migrada.
- `fix/isosceles-logic`: Rama utilizada para corregir el bug de lógica en la detección de isósceles y completar la cobertura al 100%. Esta rama fue fusionada mediante Pull Request.

## 👥 Autores

- Pablo Manglano Redondo
- Mario Toledano Borda
- Daniel Candeleda Martín-Moyano
