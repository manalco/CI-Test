from app import calcular_prioridad


def test_prioridad_normal():
    # Caso base: 3 días debe ser prioridad Normal
    assert calcular_prioridad(3) == "Normal"


def test_prioridad_alta():
    # Caso límite: 6 días debe ser prioridad Alta
    assert calcular_prioridad(6) == "Alta"


def test_dias_negativos():
    # Validación de error
    assert calcular_prioridad(-1) == "Error: Días negativos"
