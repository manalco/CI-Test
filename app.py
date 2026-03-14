def calcular_prioridad(dias_abierto):
    """
    Calcula la prioridad basado en los días que lleva abierto un ticket.
    Prioridad Alta: > 5 días
    Prioridad Normal: <= 5 días
    """
    if dias_abierto < 0:
        return "Error: Días negativos"

    if dias_abierto > 5:
        return "Alta"
    else:
        return "Normal"
