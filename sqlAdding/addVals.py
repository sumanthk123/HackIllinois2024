import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")        


# create_database_query = 'CREATE DATABASE model_values'
# connection = create_server_connection('localhost', 'root', 'Pik@chu1423')
# create_database(connection, create_database_query)
connection = create_db_connection('localhost', 'root', 'Pik@chu1423', 'CHATGDP')
q1 = 'SELECT * FROM model_values'
#results = read_query(connection, q1)
increment = 'UPDATE model_values SET price = price + 1 WHERE model_name = "gpt-4-0125-preview"'
results = execute_query(connection, increment)

showResults = read_query(connection, q1)
for result in showResults:
    print(result)
