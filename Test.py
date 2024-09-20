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
        cursor.execute ('Insert')
        conn.commit()
        conn.close()

def update_run_counter(new_count):
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()

        # Update the count
        cursor.execute('UPDATE run_counter SET count = ? WHERE rowid = 1', (new_count,))

        conn.commit()  # Save the changes
        conn.close()

AWS_SECRET_ACCESS_KEY='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'