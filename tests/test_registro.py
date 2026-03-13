import pytest
from src.ciudadanos.registro import RegistroPersonas


def datos():
    return [
        ('111', 'Pedro', 'Paez', 24),
        ('222', 'Ana', 'Lopez', 30),
        ('333', 'Juan', 'Perez', 18),
    ]


def test_promedio_edad():
    registro = RegistroPersonas(datos())
    assert registro.promedio_edad() == pytest.approx(24)


def test_persona_mayor():
    registro = RegistroPersonas(datos())
    assert registro.persona_mayor_edad().edad == 30


def test_persona_menor():
    registro = RegistroPersonas(datos())
    assert registro.persona_menor_edad().edad == 18


def test_segmentacion():
    registro = RegistroPersonas(datos())
    menores, mayores = registro.segmentar_por_edad(25)
    assert len(menores) == 2
    assert len(mayores) == 1


def test_dni_duplicado():
    with pytest.raises(ValueError):
        RegistroPersonas([
            ('111', 'Pedro', 'Paez', 24),
            ('111', 'Juan', 'Perez', 20),
        ])
