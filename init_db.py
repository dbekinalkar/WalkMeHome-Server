import os
import psycopg


conn = psycopg.connect(os.environ['DATABASE_URL'])
# conn = psycopg.connect(
#         host=os.environ['DATABASE_URL'],
#         database="WalkMeHomeDB",
#         user=os.environ['DB_USERNAME'],
#         password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS Users;')
cur.execute('CREATE TABLE Users (id serial PRIMARY KEY,'
                                'username VARCHAR(24) NOT NULL,'
	                            'password VARCHAR(24) NOT NULL,'
	                            'email VARCHAR(40) NOT NULL,'
	                            'trip VARCHAR,'
                                 ');'
                                 )

# Insert data into the table

cur.execute('INSERT INTO Users (username, password, email, trip)'
            'VALUES (%s, %s, %s, %s)',
            ('Daniyal',
             'DaniyalTheGoatFr',
             'daniyal_the_goat@gmail.com',
             None)
            )


conn.commit()

cur.close()
conn.close()