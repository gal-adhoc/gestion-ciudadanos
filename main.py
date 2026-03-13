from src.ciudadanos.registro import RegistroPersonas


datos = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Ana', 'Lopez', 30),
    ('33333333', 'Juan', 'Perez', 18),
    ('44444444', 'Maria', 'Garcia', 40),
]

registro = RegistroPersonas(datos)

print("Registros formateados:")
print(registro.formatear_registros())

print("\nPersona con mayor edad:")
print(registro.persona_mayor_edad())

print("\nPersona con menor edad:")
print(registro.persona_menor_edad())

menores, mayores = registro.segmentar_por_edad()

print("\nMenores de 25:")
print(menores)

print("\nMayores o iguales a 25:")
print(mayores)

print("\nPromedio edad:")
print(registro.promedio_edad())

print("\nEdad por DNI 11111111:")
print(registro.edad_por_dni('11111111'))
