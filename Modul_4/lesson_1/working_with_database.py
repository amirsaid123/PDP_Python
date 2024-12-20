import psycopg2

conn = psycopg2.connect(host="localhost", dbname="amirsaid_db", user="postgres", password="1234", port=5432)

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users (
             id serial PRIMARY KEY,
             name varchar(255),
             age int NOT NULL,
             gender CHAR(1)
)
""")

# cur.execute(""" INSERT INTO users (name, age, gender) VALUES
# ('Mike', 54, 'M'),
# ('John', 24, 'M'),
# ('Amir', 14, 'M'),
# ('David', 37, 'M'),
# ('Solomon', 41, 'M'),
# ('Mason', 25, 'M')
# """)
#


cur.execute(""" select * from users where age < 50;""")

for row in cur.fetchall():
    print(row)

print(cur.fetchone())







conn.commit()

cur.close()
conn.close()
