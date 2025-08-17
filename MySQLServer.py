import mysql.connector
from mysql.connector import Error

def create_database (host, user, password, db_name):
  connection = None
  try:
    connection= mysql.connector.connect(
      host=host,
      user=user,
      password=password
)
    print("Connection to MYSQL DB successful")

    cursor=connection.cursor()
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
    cursor.execute(create_db_query)
    print(f"Database '{db_name}' created successfully!")
  
  except Error as err:
    print (f"Failed to connect to the DB: {err}")
  
  finally:
    if connection and connection.is_connected():
      cursor.close()
      connection.close()
      print("MySQL connection is closed.")
    
DB_Host= "localhost"
DB_USER= "root"
DB_PASS= "RSV_lloyd_khanyi@123"
DATABASE_NAME= "alx_book_store"

create_database(DB_Host, DB_USER, DB_PASS, DATABASE_NAME)