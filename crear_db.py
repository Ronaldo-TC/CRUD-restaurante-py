import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

# Crear la tabla "Platos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Platos (
        nombre TEXT PRIMARY KEY,
        precio REAL
    )
''')

# Crear la tabla "Mesas"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mesas (
        numero INTEGER PRIMARY KEY
    )
''')

# Crear la tabla "Pedidos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plato TEXT,
        mesa INTEGER,
        cantidad INTEGER,
        fecha TEXT,
        FOREIGN KEY (plato) REFERENCES Platos(nombre),
        FOREIGN KEY (mesa) REFERENCES Mesas(numero)
    )
''')

# Insertar 5 platos
platos = [
    ('Pizza Margarita', 15.50),
    ('Ensalada César', 8.75),
    ('Pasta Carbonara', 12.00),
    ('Hamburguesa', 10.00),
    ('Lasagna', 14.00)
]
cursor.executemany("INSERT INTO Platos (nombre, precio) VALUES (?, ?)", platos)

# Insertar 5 mesas
mesas = [(1,), (2,), (3,), (4,), (5,)]
cursor.executemany("INSERT INTO Mesas (numero) VALUES (?)", mesas)

# Insertar 5 pedidos
pedidos = [
    ('Pizza Margarita', 1, 2, '2024-03-09'),
    ('Ensalada César', 2, 1, '2024-03-09'),
    ('Pasta Carbonara', 3, 3, '2024-03-09'),
    ('Hamburguesa', 4, 1, '2024-03-09'),
    ('Lasagna', 5, 2, '2024-03-09')
]
cursor.executemany(
    "INSERT INTO Pedidos (plato, mesa, cantidad, fecha) VALUES (?, ?, ?, ?)", pedidos)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
