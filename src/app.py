import psycopg2
import os
from dotenv import load_dotenv


def connect():
    try:
        connection = psycopg2.connect( 
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
    except Exception as e:
        print("Connection failed", e)
        return None
    if connection:
        print("Connection established successfully")
        return connection

def execute_sql_file(file_path, connection):
    cursor = connection.cursor()
    sql_file = open(file_path)
    cursor.execute(sql_file.read())
    connection.commit()
    cursor.close()

def db_initial_setup(connection):
    execute_sql_file('./ddl.sql', connection)
    print("DB set up executed successfully")

def main():
    connection = connect()
    if connection:
        db_initial_setup(connection)
        connection.close()


if __name__ == '__main__':
    load_dotenv()
    main()