import pymysql

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)

cursor = client.cursor()
# cursor.execute('''
#     CREATE TABLE d4e11.centre(
#         id VARCHAR(255) UNIQUE PRIMARY KEY,
#         name VARCHAR(255) UNIQUE
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE d4e11.salesman(
#         username VARCHAR(255) PRIMARY KEY,
#         centre_id VARCHAR(255) REFERENCES d4e11.centre(id),
#         email VARCHAR(255),
#         name VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     INSERT INTO d4e11.centre(id,name)
#     VALUES('1','bac'),('2','trung'),('3','nam');
# ''')
centre_name = 'bac'
cursor.execute(f''' SELECT id FROM d4e11.centre WHERE name ='{centre_name}' ''' ) #f : string formating
centre_found = cursor.fetchone()

cursor.execute(f'''
    INSERT INTO d4e11.salesman(username,centre_id,email,name) 
    VALUES('best salesman','{centre_found['id']}','thang@gmail.com','Thang')
''')
client.commit()