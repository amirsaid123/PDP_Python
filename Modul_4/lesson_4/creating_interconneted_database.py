import psycopg2

connection = psycopg2.connect(host='localhost', dbname='canva_data', user='postgres', password=1234, port=5432)
cursor = connection.cursor()















connection.commit()
cursor.close()
connection.close()