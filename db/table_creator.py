import psycopg2

from utilities import read_value_from_config

db = read_value_from_config('db_connection')

conn = psycopg2.connect(db)

with conn.cursor() as cursor:
    with open("results.sql", "r") as table_sql:
        cursor.execute(table_sql.read())
        conn.commit()
