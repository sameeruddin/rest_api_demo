import psycopg2

# Database connection details
DB_CONFIG = { # Enter DB connection parameters
    }

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        raise