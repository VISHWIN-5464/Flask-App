from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# -------------------- Database Setup --------------------
def init_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Product (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Location (
                    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS ProductMovement (
                    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    from_location INTEGER,
                    to_location INTEGER,
                    product_id INTEGER,
                    qty INTEGER,
                    FOREIGN KEY (from_location) REFERENCES Location(location_id),
                    FOREIGN KEY (to_location) REFERENCES Location(location_id),
                    FOREIGN KEY (product_id) REFERENCES Product(product_id)
                )''')
    conn.commit()
    conn.close()

# -------------------- Helper --------------------
def get_db_connection():
    return sqlite3.connect('inventory.db')

# -------------------- Product Routes --------------------
@app.route('/products', methods=['GET', 'POST'])
def products():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        c.execute('INSERT INTO Product (name) VALUES (?)', (name,))
        conn.commit()
        return redirect('/products')

    c.execute('SELECT * FROM Product')
    products = c.fetchall()
    conn.close()
    return render_template('products.html', products=products)

# -------------------- Location Routes --------------------
@app.route('/locations', methods=['GET', 'POST'])
def locations():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        c.execute('INSERT INTO Location (name) VALUES (?)', (name,))
        conn.commit()
        return redirect('/locations')

    c.execute('SELECT * FROM Location')
    locations = c.fetchall()
    conn.close()
    return render_template('locations.html', locations=locations)

# -------------------- Product Movement --------------------
@app.route('/movements', methods=['GET', 'POST'])
def movements():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('SELECT * FROM Product')
    products = c.fetchall()
    c.execute('SELECT * FROM Location')
    locations = c.fetchall()

    if request.method == 'POST':
        product_id = request.form['product_id']
        from_loc = request.form.get('from_location') or None
        to_loc = request.form.get('to_location') or None
        qty = int(request.form['qty'])

        c.execute('INSERT INTO ProductMovement (timestamp, from_location, to_location, product_id, qty) VALUES (?,?,?,?,?)',
                  (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), from_loc, to_loc, product_id, qty))
        conn.commit()
        return redirect('/movements')

    c.execute('SELECT * FROM ProductMovement')
    movements = c.fetchall()
    conn.close()
    return render_template('movements.html', movements=movements, products=products, locations=locations)

# -------------------- Report --------------------
@app.route('/report')
def report():
    conn = get_db_connection()
    c = conn.cursor()

    query = """
    SELECT p.name AS product, l.name AS location,
           IFNULL(SUM(CASE WHEN pm.to_location = l.location_id THEN pm.qty ELSE 0 END), 0) -
           IFNULL(SUM(CASE WHEN pm.from_location = l.location_id THEN pm.qty ELSE 0 END), 0) AS qty
    FROM Product p
    CROSS JOIN Location l
    LEFT JOIN ProductMovement pm ON pm.product_id = p.product_id
    GROUP BY p.product_id, l.location_id
    HAVING qty != 0
    ORDER BY p.name, l.name
    """
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return render_template('report.html', rows=rows)

@app.route('/')
def home():
    return render_template('base.html')


# -------------------- Main --------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
