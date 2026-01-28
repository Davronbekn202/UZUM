import psycopg2
def get_connection():
    return psycopg2.connect(
        dbname="mini_uzum",
        user='postgres',
        password="A0B1D9E2",
        host='localhost',
        port=5432
    )
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255),
        phone VARCHAR(20) UNIQUE,
        password VARCHAR(255),
        role VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        price NUMERIC(10,2),
        stock INT,
        category_id INT REFERENCES categories(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS carts (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cart_items (
        id SERIAL PRIMARY KEY,
        cart_id INT REFERENCES carts(id),
        product_id INT REFERENCES products(id),
        quantity INT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        total_price NUMERIC(10,2),
        status VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(id),
        product_id INT REFERENCES products(id),
        quantity INT,
        price NUMERIC(10,2)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(id),
        amount NUMERIC(10,2),
        status VARCHAR(20),
        paid_at TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id SERIAL PRIMARY KEY,
        product_id INT REFERENCES products(id),
        user_id INT REFERENCES users(id),
        rating INT,
        comment TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()






