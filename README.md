# Gestión de Ciudadanos

Sistema simple en Python para procesar registros de ciudadanos provenientes de un sistema legacy.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/gal-adhoc/gestion-ciudadanos.git
cd gestion-ciudadanos
```

### 2. Crear y activar entorno virtual (recomendado)

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el programa principal

```bash
python main.py
```

Esto mostrará:
- Registros formateados
- Persona con mayor y menor edad
- Segmentación por edad (mayores/menores de 25)
- Promedio de edad
- Consulta de edad por DNI

### Ejecutar los tests

```bash
pytest -v -s
```

Para ver cobertura de código:
```bash
pip install pytest-cov
pytest --cov=src
```

## Funcionalidades

- **Modelo inmutable de Persona** con validaciones
- **Validación de edad negativa** - No permite edades menores a 0
- **Validación de DNIs duplicados** - Detecta y rechaza registros duplicados
- **Formateo de registros** - Convierte datos a formato diccionario
- **Consulta de extremos de edad** - Obtiene persona mayor y menor
- **Segmentación por edad** - Divide población según umbral (default: 25 años)
- **Cálculo de promedio de edad** - Métrica estadística básica
- **Acceso eficiente O(1)** - Consulta de edad por DNI en tiempo constante

## Estructura del Proyecto

```
gestion_ciudadanos/
├── src/
│   └── ciudadanos/
│       ├── models.py        # Modelo Persona
│       └── registro.py      # Lógica de procesamiento
├── tests/
│   └── test_registro.py     # Tests unitarios
├── main.py                  # Script principal
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```
