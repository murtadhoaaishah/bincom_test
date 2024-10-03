import psycopg2

def connect_db():
    """Establishes a connection to the PostgreSQL database and returns the connection and cursor."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="color_analysis",
            user="your_username",
            password="your_password"
        )
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None, None

def create_table(cur):
    """Creates the color frequencies table if it doesn't exist."""
    cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(20),
        frequency INT
    )
    """)

def insert_color_data(cur, color, frequency):
    """Inserts color frequency data into the PostgreSQL table."""
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

def close_connection(conn, cur):
    """Closes the database connection."""
    cur.close()
    conn.close()