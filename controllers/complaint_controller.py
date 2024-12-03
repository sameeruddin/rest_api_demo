from .db_connection import get_db_connection
from psycopg2.extras import RealDictCursor

def create_complaint(customer_id, category, description, priority, engineer_id):
    query = """ INSERT INTO complaints (customer_id, engineer_id, category, description, priority) VALUES (%s, %s, %s, %s, %s); """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (customer_id, engineer_id, category, description, priority))
            conn.commit()
    except Exception as e:
        print("Error creating complaint:", e)
    finally:
        conn.close()

def get_all_complaints():
    query = "SELECT * FROM complaints;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            complaint = cursor.fetchall()
            return complaint
    except Exception as e:
        print("Error fetching complaint:", e)
    finally:
        conn.close()

def get_complaint(complaint_id):
    query = "SELECT * FROM complaints WHERE complaint_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (complaint_id,))
            complaint = cursor.fetchone()
            return complaint
    except Exception as e:
        print("Error fetching complaint:", e)
    finally:
        conn.close()

def update_complaint(complaint_id, status, engineer_id):
    query = """
    UPDATE complaints
    SET status = COALESCE(%s, status),
        engineer_id = COALESCE(%s, engineer_id),
        updated_at = CURRENT_TIMESTAMP
    WHERE complaint_id = %s RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (status, engineer_id, complaint_id))
            complaint = cursor.fetchone()
            conn.commit()
            return complaint
    except Exception as e:
        print("Error updating complaint:", e)
    finally:
        conn.close()

def delete_customer(complaint_id):
    query = "DELETE FROM complaints WHERE complaint_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, (complaint_id,))
            conn.commit()
    except Exception as e:
        print("Error deleting complaint:", e)
    finally:
        conn.close()