from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- PLATOS ---

# Obtener todos los platos (para mostrar en la página principal)


@app.route('/')
def index():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Platos")
    platos = cursor.fetchall()
    conn.close()
    return render_template('index.html', platos=platos)


@app.route('/platos')
def platos():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Platos")
    platos = cursor.fetchall()
    conn.close()
    return render_template('platos/index.html', platos=platos)
# Crear un nuevo plato


@app.route('/crear_plato', methods=['POST'])
def crear_plato():
    nombre = request.form['nombre']
    precio = request.form['precio']
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Platos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
    except sqlite3.IntegrityError:
        # Manejar el error si ya existe un plato con ese nombre (opcional)
        pass
    finally:
        conn.close()
    return redirect(url_for('index'))

# Actualizar un plato existente


@app.route('/actualizar_plato/<nombre>', methods=['POST'])
def actualizar_plato(nombre):
    precio = request.form['precio']
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Platos SET precio = ? WHERE nombre = ?", (precio, nombre))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Eliminar un plato


@app.route('/eliminar_plato/<nombre>', methods=['POST'])
def eliminar_plato(nombre):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Platos WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# --- MESAS ---


# Obtener todas las mesas
@app.route('/mesas')
def mesas():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mesas")
    mesas = cursor.fetchall()
    conn.close()
    return render_template('mesas/index.html', mesas=mesas)

# Crear una nueva mesa


@app.route('/crear_mesa', methods=['POST'])
def crear_mesa():
    numero = request.form['numero']
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Mesas (numero) VALUES (?)", (numero,))
        conn.commit()
    except sqlite3.IntegrityError:
        # Manejar el error si ya existe una mesa con ese número (opcional)
        pass
    finally:
        conn.close()
    return redirect(url_for('mesas'))

# Actualizar una mesa existente


@app.route('/actualizar_mesa/<numero>', methods=['POST'])
def actualizar_mesa(numero):
    nuevo_numero = request.form['numero']
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Mesas SET numero = ? WHERE numero = ?",
                   (nuevo_numero, numero))
    conn.commit()
    conn.close()
    return redirect(url_for('mesas'))

# Eliminar una mesa


@app.route('/eliminar_mesa/<numero>', methods=['POST'])
def eliminar_mesa(numero):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Mesas WHERE numero = ?", (numero,))
    conn.commit()
    conn.close()
    return redirect(url_for('mesas'))

# --- PEDIDOS ---

# Obtener todos los pedidos


@app.route('/pedidos')
def pedidos():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return render_template('pedidos/index.html', pedidos=pedidos)

# Crear un nuevo pedido


@app.route('/crear_pedido', methods=['POST'])
def crear_pedido():
    plato = request.form['plato']
    mesa = request.form['mesa']
    cantidad = request.form['cantidad']
    fecha = request.form['fecha']
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Pedidos (plato, mesa, cantidad, fecha) VALUES (?, ?, ?, ?)",
                       (plato, mesa, cantidad, fecha))
        conn.commit()
    except sqlite3.IntegrityError:
        # Manejar el error si hay algún problema con la integridad referencial (opcional)
        pass
    finally:
        conn.close()
    return redirect(url_for('pedidos'))

# Actualizar un pedido existente


@app.route('/actualizar_pedido/<id>', methods=['POST'])
def actualizar_pedido(id):
    # Obtener los nuevos datos del formulario
    # ...
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    # Actualizar el pedido en la base de datos
    # ...
    conn.commit()
    conn.close()
    return redirect(url_for('pedidos'))

# Eliminar un pedido


@app.route('/eliminar_pedido/<id>', methods=['POST'])
def eliminar_pedido(id):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pedidos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('pedidos'))


if __name__ == '__main__':
    app.run(debug=True)
