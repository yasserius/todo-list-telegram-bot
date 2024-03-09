from sqlalchemy import create_engine, text
import os


def get_vercel_db_conn():
    # todo: replace with os.getenv('DATABASE_URL')
    return create_engine(os.get)

def create_payments_table():
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        create_query = text('''
            CREATE TABLE IF NOT EXISTS Todos (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT,
                text VARCHAR(100)
            );
            CREATE INDEX telegram_id_index ON Todos (telegram_id);
        ''')
        conn.execute(create_query)
        print('created todos table')
        conn.commit()

def delete_payments_table():
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        drop_query = text('DROP TABLE IF EXISTS Todos')
        conn.execute(drop_query)
        print('deleted todos table')
        conn.commit()

def add_new_todo(todo_dict):
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        query = text("""
            INSERT INTO Todos (telegram_id, text) 
            VALUES (:telegram_id, :text)
        """)
        conn.execute(query, todo_dict)
        conn.commit()
    engine.dispose()

def delete_todo_by_id(id, telegram_id):
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        query = text("""
            DELETE FROM Todos
            WHERE id = :id AND telegram_id = :telegram_id
        """)
        conn.execute(query, dict(id=id, telegram_id=telegram_id))
        conn.commit()
    engine.dispose()

def get_recent_todos():
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        # Retrieve the 10 most recent payments
        result = conn.execute(text('''
            SELECT *
            FROM Todos
            ORDER BY id DESC
            LIMIT 10
        '''))
        
        # Print the recent payment rows
        output = [p for p in result]
        conn.close()
    engine.dispose()
    return output

def get_todos_by_telegram_id(telegram_id):
    engine = get_vercel_db_conn()
    with engine.connect() as conn:
        result = conn.execute(
            text('''
                SELECT *
                FROM Todos
                WHERE telegram_id = :telegram_id
                ORDER BY id DESC
            '''),
            dict(telegram_id=telegram_id)    
        )
        
        output = [p for p in result]
        conn.close()
    engine.dispose()
    return output


if __name__ == '__main__':
    create_payments_table()
