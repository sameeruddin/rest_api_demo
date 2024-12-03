from .db_connection import get_db_connection
from psycopg2.extras import RealDictCursor

def create_customer(name, email, phone_number):
    query = """
    INSERT INTO customers (name, email, phone_number)
    VALUES (%s, %s, %s);
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (name, email, phone_number))
            conn.commit()
    except Exception as e:
        print("Error creating customer:", e)
    finally:
        conn.close()

def get_customer(customer_id):
    query = "SELECT * FROM customers WHERE customer_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (customer_id,))
            customer = cursor.fetchone()
            return customer
    except Exception as e:
        print("Error fetching customer:", e)
    finally:
        conn.close()

def get_all_customers():
    query = "SELECT * FROM customers;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            customer = cursor.fetchall()
            return customer
    except Exception as e:
        print("Error fetching customers:", e)
    finally:
        conn.close()

def update_customer(customer_id, name, email, phone_number):
    query = """
    UPDATE customers
    SET name = COALESCE(%s, name),
        email = COALESCE(%s, email),
        phone_number = COALESCE(%s, phone_number),
        updated_at = CURRENT_TIMESTAMP
    WHERE customer_id = %s RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (name, email, phone_number, customer_id))
            customer = cursor.fetchone()
            conn.commit()
            return customer
    except Exception as e:
        print("Error updating customer:", e)
    finally:
        conn.close()

def delete_customer(customer_id):
    query = "DELETE FROM customers WHERE customer_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, (customer_id,))
            conn.commit()
    except Exception as e:
        print("Error deleting customer:", e)
    finally:
        conn.close()
