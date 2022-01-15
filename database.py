import psycopg2
from psycopg2.extras import DictCursor


def sql_select(query, params):
    conn = psycopg2.connect("dbname=project2")
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def sql_write(query, params):
    conn = psycopg2.connect("dbname=project2")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()


# from original app.py
# conn = psycopg2.connect(DB_URL)
# cur = conn.cursor()
# cur.execute('SELECT 1', [])  # Query to check that the DB connected
# conn.close()
