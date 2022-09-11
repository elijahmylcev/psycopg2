from multiprocessing import connection
import psycopg2
from config import host, user, password, db_name

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

except Exception as _ex:
  print('[INFO] Error while with PostgreSQL', _ex)
finally:
  if connection:
    connection.close()
    print('[INFO] PostgreSQL connection closed')