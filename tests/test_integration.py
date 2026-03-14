import sqlite3
from app import calcular_prioridad


def test_db_connection_and_ticket_creation():
    # 1. Configurar conexión (Integración con DB)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE tickets (id INTEGER, ubicacion TEXT, prioridad TEXT)'
    )

    # 2. Lógica de negocio + Persistencia
    ubicacion = "Laboratorio de Redes"
    prioridad = calcular_prioridad(10)  # Dos espacios antes del comentario

    cursor.execute(
        'INSERT INTO tickets (id, ubicacion, prioridad) VALUES (?, ?, ?)',
        (1, ubicacion, prioridad)
    )
    conn.commit()

    # 3. Verificación (Assert)
    cursor.execute('SELECT prioridad FROM tickets WHERE id=1')
    resultado = cursor.fetchone()

    assert resultado[0] == "Alta"
    conn.close()
