import pymysql
from pymongo import *
mongo_client = MongoClient()
db = mongo_client.get_database('mysql_ex')
collection = db.get_collection('restaurants')
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)
cursor = mysql_client.cursor()
# cursor.execute('''
#     CREATE TABLE restaurants.restaurant(
#     restaurant_id VARCHAR(255) PRIMARY KEY,
#     name VARCHAR(255),
#     cuisine VARCHAR(255),
#     borough VARCHAR(255),
#     building VARCHAR(255),
#     street VARCHAR(255),
#     zipcode VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE restaurants.grades(
#         grade_id INT(11) AUTO_INCREMENT PRIMARY KEY,
#         restaurant_id VARCHAR(255),
#         date VARCHAR(255),
#         grade VARCHAR(255),
#         score INT(4)
#     )
# ''')
data_restaurant = collection.find()
# for data in data_restaurant:
#     data_id = str(data['_id'])
#     cursor.execute(f'''
#         INSERT INTO restaurants.restaurant(
#             restaurant_id,
#             name,
#             cuisine,
#             borough,
#             building,
#             street,
#             zipcode
#         )
#         VALUES(
#             "{data['restaurant_id']}",
#             "{data['name']}",
#             "{data['cuisine']}",
#             "{data['borough']}",
#             "{data['address']['building']}",
#             "{data['address']['street']}",
#             "{data['address']['zipcode']}"

#         )
#     ''')
# for data in data_restaurant:
#     for grade_find in data['grades']:
#         # print(data['restaurant_id'],grade_find['date'],grade_find['grade'],grade_find['score'])
#         cursor.execute(f'''
#             INSERT INTO restaurants.grades(
#                 restaurant_id,
#                 date,
#                 grade,
#                 score
#             )
#             VALUES(
#                 "{data['restaurant_id']}",
#                 "{grade_find['date']}",
#                 "{grade_find['grade']}",
#                 "{grade_find['score']}"
#             )
#         ''')
mysql_client.commit()