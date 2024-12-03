from .db_connection import get_db_connection
from psycopg2.extras import RealDictCursor

def create_job(complaint_id, engineer_id, status, comment):
    query = """
    INSERT INTO jobs (complaint_id, engineer_id, status, comment)
    VALUES (%s, %s, %s, %s) RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (complaint_id, engineer_id, status, comment))
            job = cursor.fetchone()
            conn.commit()
            return job
    except Exception as e:
        print("Error creating job:", e)
    finally:
        conn.close()

def get_all_jobs():
    query = "SELECT * FROM jobs;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            complaint = cursor.fetchall()
            return complaint
    except Exception as e:
        print("Error fetching jobs:", e)
    finally:
        conn.close()

def get_status_jobs(job_status):
    query = "SELECT * FROM jobs WHERE status =%s;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (job_status,))
            jobs = cursor.fetchall()
            return jobs
    except Exception as e:
        print("Error fetching jobs:", e)
    finally:
        conn.close()

def get_job(job_id):
    query = "SELECT * FROM jobs WHERE job_id = %s;"
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (job_id,))
            job = cursor.fetchone()
            return job
    except Exception as e:
        print("Error fetching job:", e)
    finally:
        conn.close()

def update_job(job_id, status=None, comment=None):
    query = """
    UPDATE jobs
    SET status = COALESCE(%s, status),
        comment = COALESCE(%s, comment),
        updated_at = CURRENT_TIMESTAMP
    WHERE job_id = %s RETURNING *;
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (status, comment, job_id))
            job = cursor.fetchone()
            conn.commit()
            return job
    except Exception as e:
        print("Error updating job:", e)
    finally:
        conn.close()
