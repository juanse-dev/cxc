import psycopg2
import os
import pandas as pd
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

def read_csv(file_path):
    df = pd.read_csv(file_path, sep=';')
    for index, row in df.iterrows():
        print(row['agency_name'], row['class_title'], row['ethnicity'], row['gender'])
        if index == 10:
            break

def main():
    connection = connect()
    if connection:
        db_initial_setup(connection)
        connection.close()
    read_csv('./catalogos.csv')



if __name__ == '__main__':
    load_dotenv()
    main()