import pymysql
from pymongo import *
mongo_client = MongoClient()
db = mongo_client.get_database('mysql_ex')
collection = db.get_collection('cakes')
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)
cursor = mysql_client.cursor()
# cursor.execute('''
#     CREATE TABLE cakes.cake(
#         id VARCHAR(255) PRIMARY KEY,
#         type VARCHAR(255),
#         name VARCHAR(255),
#         ppu VARCHAR(255)
#     )


# ''')
# cursor.execute('''
#     CREATE TABLE cakes.batter(
#         id VARCHAR(255) PRIMARY KEY,
#         type VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE cakes.cake_batter(
#         cake_id VARCHAR(255),
#         batter_id VARCHAR(255),
#         PRIMARY KEY (cake_id, batter_id)
#     )
# ''')


# cursor.execute('''
#     CREATE TABLE cakes.topping(
#         id VARCHAR(255) PRIMARY KEY,
#         type VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE cakes.cake_topping(
#         id_cake VARCHAR(255),
#         id_topping VARCHAR(255),
#         PRIMARY KEY (id_cake, id_topping)
#     )
# ''')


# cursor.execute('''
#     CREATE TABLE cakes.filling(
#         id VARCHAR(255) PRIMARY KEY,
#         name VARCHAR(255),
#         addcost VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE cakes.cake_filling(
#         id_cake VARCHAR(255),
#         id_filling VARCHAR(255),
#         PRIMARY KEY (id_cake, id_filling)
#     )
# ''')
cake_data = collection.find()
# for data in cake_data:
#     ppu = str(data['ppu'])
#     cursor.execute(f'''
#         INSERT INTO cakes.cake(id, type, name, ppu)
#         VALUES(
#             "{data['_id']}",
#             "{data['type']}",
#             "{data['name']}",
#             "{ppu}"
#         )
#      ''')
query = [
 {
    '$match': {
        'fillings': {'$ne': None}
    }
  },
  {
      '$unwind': '$fillings'
  },
  {
    '$group': {
      '_id': '$fillings', 
    }
  }
]
for filling in collection.aggregate(query):
    for id in filling['_id']['filling']:
        print(id)
mysql_client.commit()