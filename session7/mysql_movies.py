import pymysql
from pymongo import *
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('movies')
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)
cursor = mysql_client.cursor()
# cursor.execute('''
#     CREATE TABLE d4e11.movies(
#         id VARCHAR(255) PRIMARY KEY,
#         title VARCHAR(255),
#         writer VARCHAR(255),
#         year VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE d4e11.actors(
#         id INT(11) AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255)
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE d4e11.movies_actors(
#         id_movie VARCHAR(255),
#         actor_name VARCHAR(255), 
#         PRIMARY KEY (id_movie, actor_name)
#     )
# ''')
query = {
    'title':{'$ne' : None},
    'writer':{'$ne': None},
    'year':{'$ne' : None},
    'actors':{'$ne': None}
}
data = collection.find(query)
# for key in data:
#     cursor.execute(f'''
#     INSERT INTO d4e11.movies(id,title,writer,year) 
#     VALUES('{key['_id']}','{key['title']}','{key['writer']}','{key['year']}')
# ''')
all_actors = collection.distinct('actors')
for act in all_actors:
    print(act,1)
# for act in all_actors:
#     cursor.execute(f'''
#     INSERT INTO d4e11.actors(name)
#     VALUES('{act}')
# ''')
cursor.execute('''SELECT name FROM d4e11.actors''')
actor_name = cursor.fetchall()
# for key in actor_name:
#     movie_name_found = collection.find({'actors':key['name']})
#     for names in movie_name_found:
#         cursor.execute(f'''
#         INSERT INTO d4e11.movies_actors(id_movie,actor_name)
#         VALUES('{names['_id']}','{key['name']}')
#         ''')
mysql_client.commit()