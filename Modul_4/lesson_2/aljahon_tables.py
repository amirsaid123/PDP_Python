import psycopg2


conn = psycopg2.connect(
    host="localhost",
    dbname="home_work",
    user="postgres",
    password="1234",
    port=5432
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
)
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    parent_category_id INT NOT NULL REFERENCES Categories(category_id) ON DELETE CASCADE,
    stock_status BOOLEAN NOT NULL,
    image_url VARCHAR(500)
)
""")


# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Uy uchun',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Bolalar uchun',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Sovg`a',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Ayollar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Erkaklar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Davolovchi maxsulotlar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Fitnes',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Davolovchi mazlar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Mashina uchun',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Kitoblar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Aqlli soatlar',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Atir',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Yangi yel maxsulotlari',))
#
# cur.execute("""
# INSERT INTO Categories (name)
# VALUES (%s);
# """, ('Elektronika',))
#
#
#
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Sharbat tayyorlagich", "Uy sharoitida sharbat tayyorlashga yordam beradi", 169.00, 1, True, "https://example.com/sharbat_tayyorlagich"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Bolalar uchun kiyim", "Rang-barang va qulay bolalar kiyimlari", 249.00, 2, True, "https://example.com/bolalar_kiyim"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Ayollar uchun sumka", "Shikoyatli ayollar sumkasi", 450.00, 4, True, "https://example.com/ayollar_sumka"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Erkaklar futbolkasi", "Klasik erkak futbolkasi", 199.00, 5, True, "https://example.com/erkaklar_futbolka"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Sovg'a to'plami", "Maxsus sovg'a to'plami", 999.00, 3, True, "https://example.com/sovga_toplami"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Smartfon", "Yangi modeldagi smartfon", 1500.00, 14, True, "https://example.com/smartfon"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Fitnes uchun apparat", "Jismoniy holatni yaxshilash uchun moslama", 800.00, 7, True, "https://example.com/fitnes_apparat"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Yangi atir", "O'ziga xos yangi atir", 300.00, 12, True, "https://example.com/yangi_atir"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Kitoblar to'plami", "Ilmiy va badiiy kitoblar to'plami", 1200.00, 10, True, "https://example.com/kitoblar_toplami"))
#
# cur.execute("""
# INSERT INTO Products (name, description, price, parent_category_id, stock_status, image_url)
# VALUES (%s, %s, %s, %s, %s, %s);
# """, ("Aqlli soat", "Yangi dizayndagi aqlli soat", 600.00, 11, True, "https://example.com/aqlli_soat"))
#
#









conn.commit()
cur.close()
conn.close()
