import sqlite3

#Hello world
def get_db_connection():
    try:
        conn = sqlite3.connect('autoscraper.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def initialize_db():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS run_counter (
                count INTEGER
            )
        ''')
        cursor.execute
def get_first_run_count():
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT count FROM run_counter LIMIT 1')
        result = cursor.fetchone()  # Retrieve the first row
        return result[0] if result else None  # Return the count or None if no result

SQL_Query = "checking"     
AWS_SECRET_ACCESS_KEY='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
