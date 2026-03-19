# Gestión de Ciudadanos

Sistema simple en Python para procesar registros de ciudadanos provenientes de un sistema legacy.

## Requisitos

Python 3.10+

## Ejecutar el programa

python main.py

## Ejecutar los tests

pip install pytest
pytest -v -s

## Funcionalidades

- Modelo inmutable de Persona
- Validación de edad negativa
- Validación de DNIs duplicados
- Formateo de registros
- Persona con mayor y menor edad
- Segmentación por edad
- Promedio de edad
- Consulta de edad por DNI en O(1)
