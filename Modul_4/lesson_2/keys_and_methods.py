import psycopg2


conn = psycopg2.connect(host = "localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()


cur.execute("""
create table if not exists departments (
            id serial primary key,
            name varchar(255) not null,
            location varchar(255) unique
)
""")

cur.execute("""
create table if not exists users (
            id serial primary key,
            name varchar(255) not null,
            email varchar(255) unique,
            department_id int unique,
            foreign key (department_id) references departments(id)
)
""")




# cur.execute("""
# alter table users drop column email
#
# """)

# cur.execute("""
# alter table users add email varchar(255) unique
#
# """)
#

# cur.execute("""
# truncate users
# """)

# cur.execute("""
# alter table users alter column name set data type varchar(255)
#
# """)
#
#
# cur.execute("""
# alter table users rename name to user_name
#
# """)

# cur.execute("""
# alter table users rename user_name to full_name
#
# """)

# cur.execute("""
# alter table users add constraint new_email unique (email)
#
# """)

#
# cur.execute("""
# insert into users (name, email, department_id)
# values (%s, %s, %s);
# """, ('Qodir', 'hi.com', 1))



conn.commit()
cur.close()
conn.close()