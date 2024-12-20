import psycopg2



conn = psycopg2.connect(
    host = "localhost",
    dbname = "example",
    user = "postgres",
    password = 1234,
    port = 5432
)

cur = conn.cursor()

cur.execute("""
create table if not exists categories (
id serial primary key,
name varchar(255) not null,
icon varchar(255) not null
)
""")



text = """
1.ID
2.Name
3.Icon
"""
print(text)
key = input("Choose:")


match key:
    case '1':
        old_id = int(input("Enter old ID: "))
        new_id = int(input("Enter new ID: "))
        cur.execute("""update categories set id = %s where id = %s""",(new_id,old_id)) # noqa
    case '2':
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")
        cur.execute("""update categories set name = %s where name = %s""",(new_name,old_name)) #noqa
    case '3':
        old_icon = input("Enter old icon: ")
        new_icon = input("Enter new icon: ")
        cur.execute("""update categories set icon = %s where icon = %s""", (new_icon,old_icon)) #noqa
    case _:
        print("Wrong input!")























conn.commit()
cur.close()
conn.close()