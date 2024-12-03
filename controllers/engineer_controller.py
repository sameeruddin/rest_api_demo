from .db_connection import get_db_connection
from psycopg2.extras import RealDictCursor

def create_engineer(name, designation):
    query = """
    INSERT INTO engineers (name, designation)
    VALUES (%s, %s) RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (name, designation))
            engineer = cursor.fetchone()
            conn.commit()
            return engineer
    except Exception as e:
        print("Error creating engineer:", e)
    finally:
        conn.close()

def get_engineer(engineer_id):
    query = "SELECT * FROM engineers WHERE engineer_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (engineer_id,))
            engineer = cursor.fetchone()
            return engineer
    except Exception as e:
        print("Error fetching engineer:", e)
    finally:
        conn.close()

def update_engineer(engineer_id, name, designation):
    query = """
    UPDATE engineers
    SET name = COALESCE(%s, name),
        designation = COALESCE(%s, designation),
        updated_at = CURRENT_TIMESTAMP
    WHERE engineer_id = %s RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (name, designation, engineer_id))
            engineer = cursor.fetchone()
            conn.commit()
            return engineer
    except Exception as e:
        print("Error updating engineer:", e)
    finally:
        conn.close()
