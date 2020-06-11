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
a = collection.distinct('date')
print(a)
mysql_client.commit()