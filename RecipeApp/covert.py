import sqlite3
import psycopg2



sqlite_conn = sqlite3.connect('db.sqlite3')
sqlite_cursor = sqlite_conn.cursor()

print(sqlite_conn)

pg_conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="",
    port=""
)

# pg_cursor = pg_conn.cursor()

# sqlite_table1 = 'API_ingredientsubcategory'
# sqlite_table2 = 'API_ingredient'
# pg_table1 = 'API_ingredientsubcategory'
# pg_table2 = 'API_ingredient'


# sqlite_cursor.execute(f'SELECT * FROM {sqlite_table1}')
# data_table1 = sqlite_cursor.fetchall()
# pg_cursor.executemany(f'INSERT INTO public."{pg_table1}" VALUES (%s, %s)', data_table1)

# sqlite_cursor.execute(f'SELECT * FROM {sqlite_table2}')
# data_table2 = sqlite_cursor.fetchall()
# pg_cursor.executemany(f'INSERT INTO public."{pg_table2}" VALUES (%s, %s, %s,%s)', data_table2)

# # Commit and close connections
# pg_conn.commit()
# pg_conn.close()
# sqlite_conn.close()

# print("Data transfer completed.")