from multiprocessing import connection
import psycopg2
from config import host, user, password, db_name

# connection.autocommit = True

try:
  # connect to exist database
  connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
  )
  # the cursor for performing database operations

  with connection.cursor() as cursor:
    cursor.execute(
      "SELECT version();"
    )

    print(f'Server version: {cursor.fetchone()}')

  # create new table
  # with connection.cursor() as cursor:
  #   cursor.execute(
  #     """CREATE TABLE users(
  #       id serial PRIMARY KEY,
  #       first_name varchar(50) NOT NULL,
  #       nick_name varchar(50) NOT NULL);"""
  #   )
  #   connection.commit()
  #   print("[INFO] Table created successfully")

  # insert 
  with connection.cursor() as cursor:
    cursor.execute(
      """INSERT INTO users(first_name, nick_name) VALUES ('Ily', 'Elijah');"""
    )
    connection.commit()
    print("[INFO] Data was successfully inserted")
  
  # Get data from a table

except Exception as _ex:
  print('[INFO] Error while with PostgreSQL', _ex)
finally:
  if connection:
    connection.close()
    print('[INFO] PostgreSQL connection closed')