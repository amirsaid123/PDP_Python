import psycopg2

conn = psycopg2.connect(host="localhost", dbname="home_work", user="postgres", password="1234", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS category (
            category_id serial PRIMARY KEY,
            name varchar(255) NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS film_category (
            film_id serial PRIMARY KEY,
            category_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS film (
            film_id serial PRIMARY KEY,
            title varchar(255) NOT NULL,
            description text,
            release_year int,
            language_id int NOT NULL,
            rental_duration int,
            rental_rate numeric(5,2),
            length int,
            replacement_cost numeric(6,2),
            rating varchar(10),
            last_updated timestamp NOT NULL,
            special_features varchar(255),
            fulltext tsvector
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS language (
            language_id serial PRIMARY KEY,
            name varchar(20) NOT NULL,
            last_updated timestamp NOT NULL  
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS film_actor (
            actor_id serial PRIMARY KEY,
            film_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS inventory (
            inventory_id serial PRIMARY KEY,
            film_id int NOT NULL,
            store_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS rental (
            rental_id serial PRIMARY KEY,
            rental_date timestamp NOT NULL,
            inventory_id int NOT NULL,
            customer_id int NOT NULL,
            return_date timestamp,
            staff_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS payment (
            payment_id serial PRIMARY KEY,
            customer_id int NOT NULL,
            staff_id int NOT NULL,
            rental_id int NOT NULL,
            amount numeric(5,2) NOT NULL,
            payment_date timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS staff (
            staff_id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            last_name varchar(50) NOT NULL,
            address_id int NOT NULL,
            email varchar(50),
            store_id int NOT NULL,
            active boolean NOT NULL,
            username varchar(16) NOT NULL,
            password varchar(40) NOT NULL,
            last_updated timestamp NOT NULL,
            picture bytea
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS actor (
            actor_id serial PRIMARY KEY,
            first_name varchar(45) NOT NULL,
            last_name varchar(45) NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS customer (
            customer_id serial PRIMARY KEY,
            store_id int NOT NULL,
            first_name varchar(45) NOT NULL,
            last_name varchar(45) NOT NULL,
            email varchar(50),
            address_id int NOT NULL,
            active boolean NOT NULL,
            created_at timestamp NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS address (
            address_id serial PRIMARY KEY,
            address varchar(50) NOT NULL,
            address2 varchar(50),
            district varchar(20) NOT NULL,
            city_id int NOT NULL,
            postal_code varchar(10),
            phone varchar(20),
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS city (
            city_id serial PRIMARY KEY,
            city_name varchar(50) NOT NULL,
            country_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS country (
            country_id serial PRIMARY KEY,
            country_name varchar(50) NOT NULL,
            last_updated timestamp NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS store (
            store_id serial PRIMARY KEY,
            manager_staff_id int NOT NULL,
            address_id int NOT NULL,
            last_updated timestamp NOT NULL
)""")


conn.commit()
cur.close()
conn.close()
