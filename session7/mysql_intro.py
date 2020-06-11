import pymysql

client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)

cursor = client.cursor() #tao ra con tro de tro vao db

# cursor.execute('CREATE DATABASE d4e11') #tao db
# cursor.execute('''
#     CREATE TABLE d4e11.user(
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(255), 
#     age INT(11)
#     )
# ''')

#-----CREATE----
# cursor.execute('''
#     INSERT INTO d4e11.user(username, age)
#     VALUES('dat','96'),('thang',99);
# ''')


# cursor.execute('''SELECT * FROM d4e11.user''') #lenh lay data base ra
# data = cursor.fetchall() #gan toan bo db vua lay vao data
# print(data)
# client.commit()

#-----READ---------
# cursor.execute('''SELECT * FROM d4e11.user''') #lenh lay data base ra
# data = cursor.fetchone() #lay ra 1 dong dau tien trong nhung data tim dc
# #SUM, COUNT, MIN, MAX, AVG
# print(data)

#---------UPDATE-----
cursor.execute('''
    UPDATE d4e11.user SET age=1 WHERE age=96
''')

#------DELETE-------
cursor.execute('''
    DELETE FROM d4e11.user WHERE age = 99
''')
client.commit()
