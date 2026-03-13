from typing import Dict, Iterable, Tuple, List
from .models import Persona


RawPersona = Tuple[str, str, str, int]


class RegistroPersonas:

    def __init__(self, registros: Iterable[RawPersona]):
        self._personas: Dict[str, Persona] = {}

        for dni, nombre, apellido, edad in registros:
            if dni in self._personas:
                raise ValueError(f"DNI duplicado detectado: {dni}")

            persona = Persona(dni, nombre, apellido, edad)
            self._personas[dni] = persona

    def formatear_registros(self) -> Dict[str, Tuple[str, str, int]]:
        return {
            dni: (p.nombre, p.apellido, p.edad)
            for dni, p in self._personas.items()
        }

    def persona_mayor_edad(self) -> Persona:
        return max(self._personas.values(), key=lambda p: p.edad)

    def persona_menor_edad(self) -> Persona:
        return min(self._personas.values(), key=lambda p: p.edad)

    def promedio_edad(self) -> float:
        edades = [p.edad for p in self._personas.values()]
        if not edades:
            return 0
        return sum(edades) / len(edades)

    def segmentar_por_edad(self, umbral: int = 25) -> Tuple[List[Persona], List[Persona]]:
        menores = []
        mayores = []

        for persona in self._personas.values():
            if persona.edad < umbral:
                menores.append(persona)
            else:
                mayores.append(persona)

        return menores, mayores

    def edad_por_dni(self, dni: str) -> int:
        try:
            return self._personas[dni].edad
        except KeyError:
            raise KeyError(f"No existe persona con DNI {dni}")
